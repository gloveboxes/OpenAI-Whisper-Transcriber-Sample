
'''gui to call the OpenAI Whisper Transcribe Server.'''

# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb

import io
import os
import json
import base64
import datetime
from os import path
import threading
from dotenv import load_dotenv
import openai
import PySimpleGUI as sg
import requests
import speech_recognition as sr

OPENAI_MODEL_NAME = "gpt-3.5-turbo-0613"
OPENAI_MAX_TOKENS = 64
WHISPER_API_KEY_NAME = 'Api-Key'


window = None
bundle_dir = path.abspath(path.dirname(__file__))
e = threading.Event()


set_light_state = {
    "name": "set_light_state",
    "description": "Turn a light on or off and sets it to a given color and brightness",
    "parameters": {
        "type": "object",
        "properties": {
            "device": {
                "type": "string",
                "description": "The name of the light",
                "enum": ["Lounge", "bedroom", "hallway", "balcony", "kitchen", "bathroom", "toilet", "garage", "garden", "frontdoor"]
            },
            "state": {
                "type": "string",
                "enum": ["on", "off"]
            },
            "brightness": {
                "type": "string",
                "enum": ["low", "medium", "high"]
            },
            "color": {
                "type": "string",
                "enum": ["red", "white", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "indigo", "teal", "olive", "brown", "black", "grey", "silver", "gold", "bronze", "platinum", "rainbow"]
            }
        },
        "required": ["device"]
    }
}

washing_machine_state = {
    "name": "set_washing_machine_state",
    "description": "Turn the clothes washing machine on or off",
    "parameters": {
        "type": "object",
        "properties": {
            "device": {
                "type": "string",
                "description": "The name of the clothes washing machine"
            },
            "state": {
                "type": "string",
                "enum": ["on", "off"]
            },
        },
        "required": ["device", "state"]
    }
}

set_lock_state = {
    "name": "set_lock_state",
    "description": "lock or unlock something",
    "parameters": {
        "type": "object",
        "properties": {
            "device": {
                "type": "string",
                "description": "The name of the lock device"
            },
            "state": {
                "type": "string",
                "enum": ["lock", "unlock"]
            },
        },
        "required": ["device", "state"]
    }
}

get_the_time = {
    "name": "whats_the_time",
    "description": "Get the current time for a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city or timezone"
            }
        },
        "required": ["location"]
    }
}

get_weather = {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
            }
        },
        "required": ["location"]
    }
}

openai_functions = [
    set_light_state,
    washing_machine_state,
    set_lock_state,
    get_weather,
    get_the_time
]


def report_weather(function_call, function_arguments):
    '''This function is called when the assistant is asked about the weather.
    It calls the WeatherAPI to get the current weather for the location specified in the function call.
    It then calls the assistant again, this time providing the weather details as an argument.'''

    weather_response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={function_arguments['location']}", timeout=4)

    if weather_response.ok:

        # The response is a JSON object, which we parse to extract the weather data
        weather_data = weather_response.json()
        unit = function_arguments.get('unit', 'celsius')
        location = function_arguments.get('location')

        # We extract the relevant weather details from the weather data
        weather_details = {
            "temperature": weather_data['current']['temp_c'] if unit == 'celsius' else weather_data['current']['temp_f'],
            "unit": unit,
            "description": weather_data['current']['condition']['text']
        }

        # We call the OpenAI API again, this time providing the assistant with the weather details
        response_2 = openai.ChatCompletion.create(
            model=OPENAI_MODEL_NAME,
            messages=[
                {"role": "user", "content": f"What is the weather like in {location}?"},
                {"role": "assistant", "content": None, "function_call": {
                    "name": function_call, "arguments": json.dumps(function_arguments)}},
                {"role": "function", "name": function_call, "content": json.dumps(weather_details)}
            ],
            functions=[get_weather]
        )

        return response_2['choices'][0]['message']['content'], True
    else:
        return "Sorry, I couldn't find the weather for that location.", True


def set_device_state(function_call, function_arguments):
    '''Sets the state of a device'''
    device_name = function_arguments['device']
    response_2 = openai.ChatCompletion.create(
        model=OPENAI_MODEL_NAME,
        messages=[
            {"role": "user", "content": f"The {device_name} has been turned on or the color or brightness has been set?"},
            {"role": "assistant", "content": None, "function_call": {
                "name": function_call, "arguments": json.dumps(function_arguments)}},
            {"role": "function", "name": function_call,
                "content": json.dumps(function_arguments)}
        ],
        functions=[definition_map[function_call]]
    )

    return response_2['choices'][0]['message']['content'], True

def report_time(function_call, function_arguments):
    '''This function is called when the assistant is asked about the time.'''
    # get the current utc time formatted as a string
    utc_time = datetime.datetime.utcnow().strftime("%H:%M:%S")

    location = function_arguments['location']
    response_2 = openai.ChatCompletion.create(
        model=OPENAI_MODEL_NAME,
        messages=[
            {"role": "system", "content": f"You are a timezone assistant. The current utc time is {utc_time}"},
            {"role": "user", "content": f"What is the time in {location}?"},
            {"role": "assistant", "content": None, "function_call": {
                "name": function_call, "arguments": json.dumps(function_arguments)}},
            {"role": "function", "name": function_call,
                "content": json.dumps(function_arguments)}
        ],
        functions=[definition_map[function_call]]
    )

    return response_2['choices'][0]['message']['content'], True

function_map = {"get_current_weather": report_weather, "set_light_state": set_device_state,
                "set_light_color": set_device_state, "set_light_brightness": set_device_state,
                "set_washing_machine_state": set_device_state, "set_lock_state": set_device_state,
                "whats_the_time": report_time}

definition_map = {"get_current_weather": get_weather, "set_light_state": set_light_state, "set_washing_machine_state": washing_machine_state,
                  "set_lock_state": set_lock_state, "whats_the_time": get_the_time}


def record_audio(mic, recognizer):
    '''Record until silence'''

    with mic as source:

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        window.write_event_value("-RECORD_THREAD-", "Say something...")
        window.refresh()
        print("Say something...")

        audio = recognizer.listen(source, phrase_time_limit=15)

    print("Speech stopped")
    window.write_event_value("-RECORD_THREAD-", "Recording stopped...")
    window.refresh()

    return audio


def transcribe_audio_wav(wav):
    '''Transcribes the audio using the OpenAI Whisper Transcribe Server.'''
    transcription = None

    headers = {}
    headers[WHISPER_API_KEY_NAME] = WHISPER_API_KEY

    files = {
        'file': ('microphone.mp3', wav),
    }

    result = requests.post(
        f"{WHISPER_ENDPOINT}/transcribe", files=files, timeout=10, headers=headers)
    if result.status_code == 200:
        result = json.loads(result.text)
        transcription = result["transcription"].strip()

    return transcription


def get_openai_functions(text, last_assistant_message):
    '''Gets the OpenAI functions from the text.'''

    function_name = None
    arguments = None

    response_1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "You are a home automation assistant and you can only help with home automation."},
            {"role": "system", "content": "Start all responses with 'I'm a home automation assistant'."},
            {"role": "system", "content": "Device types limited to those listed in functions. Ask for the device name unsure. Device names have no spaces."},
            {"role": "system", "content": "Only use the functions you have been provided with."},
            {"role": "assistant", "content": last_assistant_message},
            {"role": "user", "content": text},
        ],
        functions=openai_functions,
        temperature=0.0,
        max_tokens=OPENAI_MAX_TOKENS
    )

    # The assistant's response includes a function call. We extract the arguments from this function call

    result = response_1.get('choices')[0].get('message')
    content = result.get("content", "")

    if result.get("function_call"):
        function_name = result.get("function_call").get("name")
        arguments = json.loads(result.get("function_call").get("arguments"))

    return content, function_name, arguments

def transcribe(audio, recognizer):
    '''Transcribes the audio.'''

    if WHISPER_MODE == "local":
        transcription = recognizer.recognize_whisper(audio, model="tiny.en")
    elif WHISPER_MODE == "openai":
        in_memory_file = io.BytesIO()
        in_memory_file.write(audio.get_wav_data())
        in_memory_file.seek(0)
        in_memory_file.name = "microphone.wav"           
        transcription = openai.Audio.transcribe( file=in_memory_file, model="whisper-1")["text"]
    elif WHISPER_MODE == "gpu":
        transcription = transcribe_audio_wav(audio.get_wav_data())

    return transcription


def state_machine(mic_index, energy_threshold):
    '''This is the pipeline thread.'''

    state_counter = 0
    max_loop = 0
    last_assistant_message = ""

    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = energy_threshold

    mic = sr.Microphone(mic_index)

    while 1:
        try:

            print("State: ", state_counter)
            # wait for the user to say something
            if e.is_set():
                max_loop += 1
                if max_loop > 20:
                    e.clear()
                    max_loop = 0
                    state_counter = 0
                    last_assistant_message = ""
                    print("Max conversation length reached. Resetting.")
                    window.write_event_value("-RECORD_THREAD-", "Microphone")
                    window.refresh()

            e.wait()

            previous_transcription = window["-TRANSCRIPTION-"].DefaultText
            previous_content = window["-CONTENT-"].DefaultText

            # record audio state
            if state_counter == 0:
                audio = record_audio(mic, recognizer)
                state_counter += 1

            # transcribe audio state
            elif state_counter == 1:

                transcription = transcribe(audio, recognizer)
                state_counter += 1

                previous_transcription = transcription + "\n" + \
                    "--------------------------------------------------" + "\n" + previous_transcription
                window.write_event_value(
                    "-TRANSCRIBE_THREAD-", previous_transcription)
                window.refresh()

            # get the function state
            elif state_counter == 2:
                if transcription == "" and last_assistant_message == "":
                    state_counter = 0
                    continue

                content, function_name, function_arguments = get_openai_functions(
                    transcription, last_assistant_message)
                if content:
                    last_assistant_message = content
                    print(last_assistant_message)
                    state_counter = 0

                    previous_content = content + "\n" + \
                        "--------------------------------------------------" + "\n" + previous_content
                    window.write_event_value(
                        "-CONTENT_THREAD-", previous_content)
                    window.refresh()

                elif function_name:
                    state_counter += 1

                    previous_content = "Function name: " + function_name + "\nFunction arguments: " + \
                        json.dumps(function_arguments) + "\n" + \
                        "--------------------------------------------------" + "\n" + previous_content
                    window.write_event_value(
                        "-CONTENT_THREAD-", previous_content)
                    window.refresh()

                else:
                    state_counter = 4

            # execute the function state
            elif state_counter == 3:
                content, stop = function_map[function_name](
                    function_name, function_arguments)
                if stop:
                    state_counter = 4
                else:
                    state_counter = 0

                if content is not None:
                    previous_content = content + "\n" + \
                        "--------------------------------------------------" + "\n" + previous_content
                    window.write_event_value(
                        "-CONTENT_THREAD-", previous_content)
                    window.refresh()

            # clean up state
            elif state_counter == 4:
                state_counter = 0
                max_loop = 0
                last_assistant_message = ""

                window.write_event_value("-RECORD_THREAD-", "Microphone")
                window.refresh()

                e.clear()

        except Exception as exception:
            print(exception)
            max_loop = 99


def main():
    '''Main function'''
    global window

    button_font = ("Arial", 14)

    config_frame = [
        [
            sg.Text("Select microphone", font=button_font),
            sg.Combo(["Microphone"], font=button_font, size=(28, 1), key="-MICROPHONE-", enable_events=True),
            sg.Text("Energy Threshold", font=button_font),
            sg.Input("4000", font=button_font, size=(10, 1), key="-ENERGY_THRESHOLD-", enable_events=True),
        ],
    ]

    record_frame = [

        [
            sg.Button("Microphone", font=button_font, size=(28, 1), key="-RECORD-", disabled=True),
        ]
    ]

    transcription_frame = [
        [
            sg.Text("Transcription", font=button_font, size=(28, 1)),
            sg.Text("Content", font=button_font, size=(28, 1), justification="right", expand_x=True),
        ],
        [
            sg.Multiline(key="-TRANSCRIPTION-", font=("Arial", 18), size=(70, 30), expand_x=True, expand_y=True),
            sg.Multiline(key="-CONTENT-", font=("Arial", 18), size=(70, 30), expand_x=True, expand_y=True)
        ],
    ]

    elements = [
        [sg.Frame('Configuration', font=button_font, layout=config_frame, expand_x=True)],
        [sg.Frame('Record audio', font=button_font, layout=record_frame, expand_x=True, element_justification='center')],
        [sg.Frame('Conversation', font=button_font, layout=transcription_frame, expand_x=True, expand_y=True)],
    ]

    path_to_dat = path.join(bundle_dir, 'icon.png')
    icon_base64 = base64.b64encode(open(path_to_dat, 'rb').read())

    window = sg.Window(title="OpenAI Whisper Audio Transcription",
                       layout=elements, icon=icon_base64,
                       auto_size_text=True, auto_size_buttons=True,
                       resizable=True, finalize=True)

    window["-MICROPHONE-"].update(values=sr.Microphone.list_microphone_names())

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-RECORD-":
            e.set()

            window["-TRANSCRIPTION-"].update("",
                                             text_color="black", background_color="white")
            window["-CONTENT-"].update("", text_color="black",
                                       background_color="white")
            window.refresh()

        if event == "-MICROPHONE-":
            window["-MICROPHONE-"].update(disabled=True)
            window["-RECORD-"].update(disabled=False)
            # get the index of the microphone from the list of microphones
            mic_index = sr.Microphone.list_microphone_names().index(values[event])
            energy_threshold = int(values["-ENERGY_THRESHOLD-"])
            t = threading.Thread(target=state_machine, args=(mic_index, energy_threshold))
            t.start()

        if event == "-ENERGY_THRESHOLD-":
            if len(values[event]) == 0:
                window["-ENERGY_THRESHOLD-"].update("0")
            elif values['-ENERGY_THRESHOLD-'][-1] not in ('0123456789'):
                window["-ENERGY_THRESHOLD-"].update("100")
            elif int(values[event]) > 6000:
                window["-ENERGY_THRESHOLD-"].update("6000")

        if event == "-TRANSCRIBE_THREAD-":
            window["-TRANSCRIPTION-"].update(values[event], text_color="black", background_color="white")

        if event == "-CONTENT_THREAD-":
            window["-CONTENT-"].update(values[event], text_color="black", background_color="white")

        if event == "-RECORD_THREAD-":
            window["-RECORD-"].update(values[event])

    window.close()


if __name__ == "__main__":

    load_dotenv()

    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    WHISPER_MODE = os.environ['WHISPER_MODE']
    WHISPER_MODE = "local" if os.environ['WHISPER_MODE'] == "" else os.environ['WHISPER_MODE']
    WHISPER_MODEL_NAME = "tiny" if os.environ['WHISPER_MODEL_NAME'] == "" else os.environ['WHISPER_MODEL_NAME']
    WHISPER_API_KEY = os.environ['WHISPER_API_KEY']
    WHISPER_ENDPOINT = os.environ['WHISPER_ENDPOINT']
    WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

    openai.api_key = OPENAI_API_KEY

    main()
