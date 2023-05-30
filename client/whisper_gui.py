'''gui to call the OpenAI Whisper Transcribe Server.'''
import glob
import json
import PySimpleGUI as sg
import requests

HOST_ADDRESS = "localhost"

# base64 encoded of icon.png for the gui. This made easier for  pyinstaller --onefile whisper_gui.py
ICON_BASE64 = b"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AABAkAAAgCABAABBAgAAggQAAAQJAAAIEgAAECQAACBIAABAkAAAgCABAABBAgAAggQAAAQJAAAIEgAAELS9xtDX5uvGqzvvW2M0wKqcf5tjqe/ptfm6ReZcapUAOHH22Bjj2BqjAVbl/Nscn339S2uvsKtcAQBAkAAAgCABAABBAgAAgnb9EeA0j4/u9ozLdc2B+aW1dwD2P+ffZjhwYD559sy0576r3bbrAfDU8cPP7/YMgL3I+bcZfvqV2/42xsh9V64AACBIAABAkAAAgCABAABBAgAAggQAAAQJAAAIEgAAECQAACBIAABAkAAAgCABAABBAgAAggQAAAQJAAAIEgAAECQAACBIAABA0PbaC+wXf5yvH987+6nFZkHBUr+pP80fWGTOfuX820wC4F3y552D44mdg2uvAfvKE+eOrL0C74DzbzO5AgCAIAEAAEECAACCvAG4AvO09dIY4zdr73GxeZpeWnsHuHLzX8fY2lO/Kd6c82//EABX4OQjtz40xnho7T1gvzh5/LZTY4yPrL0Hb8/5t3+4AgCAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEHbay8A/P+eu3Bo3POPr6+9BrBB/AMAAEECAACCBAAABAkAAAjyCBA2zM68dXwa84/X3uNiO/PWK2vvAFweAQAb5tSjt54eY5xeew9gs7kCAIAgAQAAQQIAAIIEAAAECQAACBIAABAkAAAgSAAAQJAAAIAgAQAAQQIAAIIEAAAECQAACBIAABAkAAAgSAAAQJAAAICg7bUXYG/7ybmji8x5Zef6ReYA8B8CgLf0/bOfXHsFAHaBKwAACBIAABAkAAAgyBsAxhhjTNP4+zzGH9beA4BlCADGGGM89cjhJ8cYN6y9BwDLcAUAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABG2vvQAs7fc7N4xxfu0tANYlAMh58tyd48lx59prAKzKFQAABAkAAAgSAAAQJAAAIGia53ntHQCAhfkHAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAIAEAAEECAACCBAAABAkAAAgSAAAQJAAAIEgAAECQAACAoH8D3PUYWdz+U0cAAAAASUVORK5CYII="


def parse_folder(path):
    '''Parses the folder for audio files.'''
    images = glob.glob(f'{path}/*.mp3') + \
        glob.glob(f'{path}/*.wav') + glob.glob(f'{path}/*.m4a')
    return images


def load_audio(path, window):
    '''Loads the audio file and calls the OpenAI Whisper Transcribe.'''
    text_color = "black"

    try:
        # disable the transcribe button
        window["-TRANSCRIBE-"].update(disabled=True)
        window.refresh()

        with open(path, 'rb') as img:
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

    window = sg.Window(title="OpenAI Whisper Audio Transcription",
                       layout=elements, icon=ICON_BASE64,
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
    try:
        with open("config.json", "r", encoding='UTF-8') as config_file:
            HOST_ADDRESS = json.load(config_file)["host_name"]
    except:
        pass

    main(host_address=HOST_ADDRESS)
