'''gui to call the OpenAI Whisper Transcribe Server.'''
import glob
import json
import PySimpleGUI as sg
import requests


WHISPER_ENDPOINT = "http://localhost:5500/transcribe"


def parse_folder(path):
    '''Parses the folder for audio files.'''
    images = glob.glob(f'{path}/*.mp3') + \
        glob.glob(f'{path}/*.wav') + glob.glob(f'{path}/*.m4a')
    return images


def load_audio(path, window):
    '''Loads the audio file and calls the OpenAI Whisper Transcribe.'''
    text_color = "black"

    try:
        with open(path, 'rb') as img:
            image_raw = img.read()

        result = requests.post(WHISPER_ENDPOINT, data=image_raw, timeout=120)

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
        print(exception)


def main():
    '''Main function'''
    font = ("Arial", 14)
    button_font = ("Arial", 12)

    elements = [
        [
            sg.FolderBrowse("Select audio folder", font=button_font , size=(20, 1)),
            sg.Input(size=(65, 1), enable_events=True, key="-FILE-",
                     font=font, tooltip="Select folder to load audio from", )
        ],
        [
            [
                sg.Button("Select file and transcribe", font=button_font, size=(20, 1),
                          key="-TRANSCRIBE-"),
                sg.Combo(key='-FILELIST-', size=(65, 20), enable_events=True, values=[],
                         font=font, tooltip="Select audio file to transcribe", readonly=True),
            ],
        ],
        [sg.Multiline(key="-TRANSCRIPTION-",
                      font=("Arial", 16), size=(85, 40))],
    ]

    window = sg.Window("OpenAI Whisper Audio Transcription",
                       elements, size=(800, 500), icon='logo.ico', auto_size_text=True, auto_size_buttons=True, resizable=True, finalize=True)
    audio_files = []

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FILE-":
            audio_files = parse_folder(values["-FILE-"])
            if audio_files:
                window['-FILELIST-'].update(values=audio_files, set_to_index=0)
        if event == '-TRANSCRIBE-':
            window["-TRANSCRIPTION-"].update(f"Transcribing {values['-FILELIST-']}",
                                             text_color="black", background_color="white")
            window.refresh()
            load_audio(values['-FILELIST-'], window)
            ch = "No"

    window.close()


if __name__ == "__main__":
    main()
