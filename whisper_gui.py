# image_browser.py

import glob
import PySimpleGUI as sg
import requests
import json

CUSTOM_VISION_ENDPOINT = "http://localhost:5000/transcribe"


def parse_folder(path):
    images = glob.glob(f'{path}/*.mp3') + \
        glob.glob(f'{path}/*.wav') + glob.glob(f'{path}/*.m4a')
    return images


def load_audio(path, window):

    try:
        with open(path, 'rb') as img:
            image_raw = img.read()

        r = requests.post(CUSTOM_VISION_ENDPOINT, data=image_raw, timeout=120)

        if r.status_code == 200:
            result = json.loads(r.text)
            if result:
                text_color = "black"
                text = (result["transcription"]).strip()
                window["-TRANSCRIPTION-"].update(
                    text, text_color=text_color, background_color="white")

    except Exception as e:
        print(e)


def main():
    font = ("Arial", 14)
    elements = [
        [
            sg.Text("Audio folder", font=font),
            sg.Input(size=(50, 1), enable_events=True, key="-FILE-",
                     font=font, tooltip="Select folder to load audio from"),
            sg.FolderBrowse(font=("Arial", 12)),
        ],
        [
            [
                sg.Text("Select file    ", font=font),
                sg.Combo(key='-FILELIST-', size=(80, 20), enable_events=True, values=[], font=font, tooltip="Select audio file to transcribe", readonly=True)],
        ],
        [sg.Text(key="-TRANSCRIPTION-", font=("Arial", 16),
                 size=(82, 25), auto_size_text=True)],
    ]

    window = sg.Window("OpenAI Whisper Audio Transcription",
                       elements, size=(1000, 700), icon='logo.ico')
    audio_files = []
    location = 0
    ch = "No"

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FILE-":
            audio_files = parse_folder(values["-FILE-"])
            if audio_files:
                window['-FILELIST-'].update(values=audio_files, set_to_index=0)
        if event == '-FILELIST-':
            ch = sg.popup_yes_no(
                f"Do you want to transcribe {values['-FILELIST-']}?", title="Confirm Transcription")
        if ch == "Yes":
            window["-TRANSCRIPTION-"].update("Transcribing",
                                             text_color="black", background_color="white")
            window.refresh()
            load_audio(values['-FILELIST-'], window)
            ch = "No"

    window.close()


if __name__ == "__main__":
    main()
