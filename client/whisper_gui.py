'''gui to call the OpenAI Whisper Transcribe Server.'''

# https://pyinstaller.org/en/stable/runtime-information.html
# pyinstaller --onefile --add-data='icon.png:.' --distpath prebuilt whisper_gui.py

import glob
import json
import base64
from os import path
import PySimpleGUI as sg
import requests


HOST_ADDRESS = "localhost"


def parse_folder(audio_path):
    '''Parses the folder for audio files.'''
    images = glob.glob(f'{audio_path}/*.mp3') + \
        glob.glob(f'{audio_path}/*.wav') + glob.glob(f'{audio_path}/*.m4a')
    return images


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

    font = ("Arial", 14)
    button_font = ("Arial", 12)

    elements = [
        [
            [
                sg.Button("Update Whisper server address",
                          font=button_font, size=(28, 1), key="-SET_HOST-"),
                sg.Input(host_address, key="-WHISPER_ENDPOINT-",
                         font=font, size=(65, 1)),
            ],
        ],
        [
            sg.FolderBrowse("Select audio folder",
                            font=button_font, size=(28, 1)),
            sg.Input(size=(65, 1), enable_events=True, key="-FILE-",
                     font=font, tooltip="Select folder to load audio from", )
        ],
        [
            [
                sg.Button("Transcribe", font=button_font, size=(28, 1),
                          key="-TRANSCRIBE-"),
                sg.Combo(key='-FILELIST-', size=(65, 20), enable_events=True, values=[],
                         font=font, tooltip="Select audio file to transcribe", readonly=True),
            ],
        ],
        [sg.Multiline(key="-TRANSCRIPTION-",
                      font=("Arial", 16), size=(95, 15))],
    ]

    bundle_dir = path.abspath(path.dirname(__file__))
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

        if event == "-SET_HOST-":
            # save the host name to a json config file
            host_address = values["-WHISPER_ENDPOINT-"]
            with open("config.json", "w", encoding='UTF-8') as config_file:
                json.dump({"host_name": host_address}, config_file)

    window.close()


if __name__ == "__main__":

    # load the host name from a json config file
    if path.exists("config.json"):
        try:
            with open("config.json", "r", encoding='UTF-8') as config_file:
                HOST_ADDRESS = json.load(config_file)["host_name"]
        except:
            pass

    main(host_address=HOST_ADDRESS)
