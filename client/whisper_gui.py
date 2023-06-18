'''gui to call the OpenAI Whisper Transcribe Server.'''

import os
from threading import Thread
import glob
import json
import base64
from os import path
import wave
import io
import pydub
import pyaudio
import PySimpleGUI as sg
import requests


STOP_RECORDING = False
HOST_ADDRESS = "http://localhost:5500"
bundle_dir = path.abspath(path.dirname(__file__))
WHISPER_API_KEY = ""
WHISPER_API_KEY_NAME = 'Api-Key'


def parse_folder(audio_path):
    '''Parses the folder for audio files.'''
    # MP3, MP4, MPEG, MPGA, M4A, WAV, and WEBM.
    audio_files = \
        glob.glob(f'{audio_path}/*.avi') + \
        glob.glob(f'{audio_path}/*.mp3') + \
        glob.glob(f'{audio_path}/*.mp4') + \
        glob.glob(f'{audio_path}/*.mpeg') + \
        glob.glob(f'{audio_path}/*.mpga') + \
        glob.glob(f'{audio_path}/*.m4a') + \
        glob.glob(f'{audio_path}/*.wav') + \
        glob.glob(f'{audio_path}/*.webm')
    
    audio_files.sort(key=lambda f: os.path.splitext(f)[1])

    return audio_files


def capture_audio(seconds, window):
    '''Captures audio from the microphone and convert to in memory mp3 file.'''
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    sample_rate = 44100  # Record at 44100 samples per second

    window.write_event_value('-RECORD_BUTTON_THREAD-', "Recording...")

    py_audio = pyaudio.PyAudio()  # Create an interface to PortAudio

    stream = py_audio.open(format=sample_format,
                    channels=channels,
                    rate=sample_rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # for i in range(0, int(fs / chunk * seconds)):
    max_seconds = int(sample_rate / chunk * seconds)
    chunks = 0

    while not STOP_RECORDING and chunks < max_seconds:
        data = stream.read(chunk)
        frames.append(data)
        chunks += 1

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    py_audio.terminate()

    # create an in-memory output file
    in_memory_output_file_wav = io.BytesIO()

    # Save the recorded data as a WAV file
    wf = wave.open(in_memory_output_file_wav, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(py_audio.get_sample_size(sample_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))

    in_memory_output_file_wav.seek(0)

    # Convert WAV to MP3
    audio = pydub.AudioSegment.from_wav(in_memory_output_file_wav)

    in_memory_output_file_mp3 = io.BytesIO()
    audio.export(in_memory_output_file_mp3, format="mp3")
    in_memory_output_file_mp3.seek(0)

    try:
        window.write_event_value('-RECORD_BUTTON_THREAD-', "Transcribing...")
        endpoint = window["-WHISPER_ENDPOINT-"].get()
        endpoint_key = window["-WHISPER_ENDPOINT_KEY-"].get()

        # add a header to the post
        headers = {}
        if endpoint_key:
            headers[WHISPER_API_KEY_NAME] = endpoint_key.strip()

        files = {
            'file': ('audio.mp3', in_memory_output_file_mp3),
        }

        result = requests.post(f"{endpoint}/transcribe", files=files, timeout=120, headers=headers)
        if result.status_code == 200:
            result = json.loads(result.text)
            if result:
                text = (result["transcription"]).strip()
                window.write_event_value("-TRANSCRIBE_THREAD-", text)
        else:
            window.write_event_value("-TRANSCRIBE_THREAD-", result.text.encode())
    except Exception as exception:
        window.write_event_value("-TRANSCRIBE_THREAD-", exception)
    finally:
        window.write_event_value('-RECORD_BUTTON_THREAD-', "Microphone")


def load_audio(audio_path, window):
    '''Loads the audio file and calls the OpenAI Whisper Transcribe.'''
    text_color = "black"

    try:
        # disable the transcribe button
        window["-TRANSCRIBE-"].update(disabled=True)
        window.refresh()

        files = {
            'file': ('audio.mp3', open(audio_path, 'rb')),
        }

        endpoint = window["-WHISPER_ENDPOINT-"].get()
        endpoint_key = window["-WHISPER_ENDPOINT_KEY-"].get()

        # add a header to the post
        headers = {}
        if endpoint_key:
            headers[WHISPER_API_KEY_NAME] = endpoint_key.strip()

        result = requests.post(
            f"{endpoint}/transcribe", files=files, timeout=120, headers=headers)

        if result.status_code == 200:
            result = json.loads(result.text)
            if result:
                text = (result["transcription"]).strip()
                window["-TRANSCRIPTION-"].update(
                    text, text_color=text_color, background_color="white")
        else:
            window["-TRANSCRIPTION-"].update(result.text.encode(),
                                             text_color=text_color, background_color="white")

    except Exception as exception:
        window["-TRANSCRIPTION-"].update(exception,
                                         text_color=text_color, background_color="white")

    finally:
        # enable the transcribe button
        window["-TRANSCRIBE-"].update(disabled=False)
        window.refresh()


def main(host_address, whisper_api_key):
    '''Main function'''
    global STOP_RECORDING

    font = ("Arial", 14)
    button_font = ("Arial", 12)

    service_config_frame = [
        [
            sg.Button("Update service config", font=button_font, size=(28, 1), key="-UPDATE_CONFIG-"),
            sg.Text("Endpoint:", font=font),
            sg.Input(host_address, key="-WHISPER_ENDPOINT-", font=font, expand_x=True),
            sg.Text("Key:", font=font),
            sg.Input(whisper_api_key, key="-WHISPER_ENDPOINT_KEY-", font=font, password_char='*', expand_x=True),
            sg.Checkbox("Show key", key="-SHOW_KEY-", font=font, enable_events=True)
        ]
    ]

    prerecorded_frame = [
        [
            sg.FolderBrowse("Audio folder", font=button_font, size=(28, 1)),
            sg.Input(size=(65, 1), enable_events=True, key="-FILE-", font=font, tooltip="Select folder to load audio from", expand_x=True)
        ],
        [
            sg.Button("Transcribe", font=button_font, size=(28, 1), key="-TRANSCRIBE-"),
            sg.Combo(key='-FILELIST-', enable_events=True, values=[], font=font, tooltip="Select audio file to transcribe", readonly=True, expand_x=True),
        ],
    ]

    record_frame = [
        [
            sg.Button("Microphone", font=button_font, size=(28, 1), key="-CAPTURE-"),
            sg.Button("Stop recording", font=button_font, size=(28, 1), key="-STOP_RECORDING-", disabled=True),
            sg.Text("Duration (seconds):", font=font, size=(16, 1)),
            sg.Input(120, size=(20, 1), key="-CAPTURE_DURATION-", font=font, expand_x=True),
        ]
    ]

    transcription_frame = [
        [
            sg.Multiline(key="-TRANSCRIPTION-", font=("Arial", 16), size=(80, 15), expand_x=True, expand_y=True)
        ]
    ]

    elements = [
        [sg.Frame('Whisper service config', font=button_font, layout=service_config_frame, expand_x=True)],
        [sg.Frame('Pre-recorded audio', font=button_font, layout=prerecorded_frame, expand_x=True)],
        [sg.Frame('Record audio', font=button_font, layout=record_frame, expand_x=True)],
        [sg.Frame('Transcription', font=button_font, layout=transcription_frame, expand_x=True, expand_y=True)],
    ]

    path_to_dat = path.join(bundle_dir, 'icon.png')
    icon_base64 = base64.b64encode(open(path_to_dat, 'rb').read())

    window = sg.Window(title="OpenAI Whisper Audio Transcription",
                       layout=elements, icon=icon_base64,
                       auto_size_text=True, auto_size_buttons=True,
                       resizable=True, finalize=True)

    audio_files = []

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-FILE-":
            audio_files = parse_folder(values["-FILE-"])
            if audio_files:
                window['-FILELIST-'].update(values=audio_files, set_to_index=0)

        if event == '-TRANSCRIBE-' and values['-FILELIST-']:
            window["-TRANSCRIPTION-"].update(f"Transcribing {values['-FILELIST-']}",
                                             text_color="black", background_color="white")
            window.refresh()
            load_audio(values['-FILELIST-'], window)

        if event == "-CAPTURE-":
            try:
                duration = int(values["-CAPTURE_DURATION-"])
            except ValueError:
                duration = 120

            window["-STOP_RECORDING-"].update(disabled=False)
            window["-TRANSCRIPTION-"].update("", text_color="black",
                                             background_color="white")
            window.refresh()

            STOP_RECORDING = False
            thread = Thread(target=capture_audio, args=(duration, window))
            thread.start()
            # capture_audio(duration, window)

        if event == "-STOP_RECORDING-":
            STOP_RECORDING = True

        if event == "-RECORD_BUTTON_THREAD-":
            window["-CAPTURE-"].update(values[event], disabled=True)
            if values[event] == "Microphone":
                window["-CAPTURE-"].update(disabled=False)
            if values[event] == "Transcribing...":
                window["-STOP_RECORDING-"].update(disabled=True)

        if event == "-TRANSCRIBE_THREAD-":
            window["-TRANSCRIPTION-"].update(values[event],
                                             text_color="black", background_color="white")

        if event == "-UPDATE_CONFIG-":
            # save the host name to a json config file
            host_address = values["-WHISPER_ENDPOINT-"]
            api_key = values["-WHISPER_ENDPOINT_KEY-"].strip()
            with open("config.json", "w", encoding='UTF-8') as config:
                json.dump({"host_name": host_address, 'whisper_api_key': api_key}, config)

        if event == "-SHOW_KEY-":
            if values["-SHOW_KEY-"]:
                window["-WHISPER_ENDPOINT_KEY-"].update(password_char="")
            else:
                window["-WHISPER_ENDPOINT_KEY-"].update(password_char="*")

    window.close()


if __name__ == "__main__":

    # load the host name from a json config file
    try:
        with open("config.json", "r", encoding='UTF-8') as config_file:
            config = json.load(config_file)
            HOST_ADDRESS = config["host_name"]
            WHISPER_API_KEY = config["whisper_api_key"]
    except Exception:
        HOST_ADDRESS = "http://localhost:5500"

    main(host_address=HOST_ADDRESS, whisper_api_key=WHISPER_API_KEY)
