'''gui to call the OpenAI Whisper Transcribe Server.'''

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
HOST_ADDRESS = "localhost"
bundle_dir = path.abspath(path.dirname(__file__))


def parse_folder(audio_path):
    '''Parses the folder for audio files.'''
    audio_files = glob.glob(f'{audio_path}/*.mp3') + \
        glob.glob(f'{audio_path}/*.wav') + glob.glob(f'{audio_path}/*.m4a')
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

        result = requests.post(
            f"http://{endpoint}:5500/transcribe", data=in_memory_output_file_mp3, timeout=120)
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
        window.write_event_value('-RECORD_BUTTON_THREAD-', "Capture audio")


def load_audio(audio_path, window):
    '''Loads the audio file and calls the OpenAI Whisper Transcribe.'''
    text_color = "black"

    try:
        # disable the transcribe button
        window["-TRANSCRIBE-"].update(disabled=True)
        window.refresh()

        with open(audio_path, 'rb') as img:
            image_raw = img.read()

        endpoint = window["-WHISPER_ENDPOINT-"].get()

        result = requests.post(
            f"http://{endpoint}:5500/transcribe", data=image_raw, timeout=120)

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


def main(host_address):
    '''Main function'''
    global STOP_RECORDING

    font = ("Arial", 14)
    button_font = ("Arial", 12)

    prerecorded_frame = [
        [
            sg.Button("Update Whisper server address", font=button_font, size=(28, 1), key="-SET_HOST-"),
            sg.Input(host_address, key="-WHISPER_ENDPOINT-", font=font, size=(65, 1), expand_x=True),
        ],
        [
            sg.FolderBrowse("Select audio folder", font=button_font, size=(28, 1)),
            sg.Input(size=(65, 1), enable_events=True, key="-FILE-", font=font, tooltip="Select folder to load audio from", expand_x=True)
        ],
        [
            sg.Button("Transcribe", font=button_font, size=(28, 1), key="-TRANSCRIBE-"),
            sg.Combo(key='-FILELIST-', size=(65, 20), enable_events=True, values=[], font=font, tooltip="Select audio file to transcribe", readonly=True, expand_x=True),
        ],
    ]

    record_frame = [
        [
            sg.Button("Capture audio", font=button_font, size=(28, 1), key="-CAPTURE-"),
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
            if values[event] == "Capture audio":
                window["-CAPTURE-"].update(disabled=False)
            if values[event] == "Transcribing...":
                window["-STOP_RECORDING-"].update(disabled=True)

        if event == "-TRANSCRIBE_THREAD-":
            window["-TRANSCRIPTION-"].update(values[event],
                                             text_color="black", background_color="white")

        if event == "-SET_HOST-":
            # save the host name to a json config file
            host_address = values["-WHISPER_ENDPOINT-"]
            with open("config.json", "w", encoding='UTF-8') as config:
                json.dump({"host_name": host_address}, config)

    window.close()


if __name__ == "__main__":

    # load the host name from a json config file
    if path.exists("config.json"):
        try:
            with open("config.json", "r", encoding='UTF-8') as config_file:
                HOST_ADDRESS = json.load(config_file)["host_name"]
        except Exception:
            HOST_ADDRESS = "localhost"

    main(host_address=HOST_ADDRESS)
