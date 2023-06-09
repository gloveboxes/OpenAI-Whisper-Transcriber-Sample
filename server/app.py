'''This is the main file of the application. It contains the Flask server and the API endpoints.'''

import random
import os
import json
import uuid
import datetime as dt
import whisper
from flask import Flask, request, jsonify


app = Flask(__name__)

MODEL = None
WHISPER_API_KEY_VALUE = None
WHISPER_API_KEY_NAME = 'Api-Key'

# https://docs.gunicorn.org/en/stable/run.html
# https://kevalnagda.github.io/flask-app-with-wsgi-and-nginx
# https://www.bing.com/search?q=delete+python+env&qs=n&form=QBRE&sp=-1&lq=0&pq=delete+python+env&sc=7-17&sk=&cvid=9772B4993AFE4BC999D0FB5CE629F5B5&ghsh=0&ghacc=0&ghpl=&ntref=1
# https://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv


def log_msg(msg):
    '''Log the request to the console.'''
    print(f"[{dt.datetime.now()}] {msg}")


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    '''Receives the audio file and returns the transcription.'''
    # check if the whisper api key is valid

    api_key = request.headers.get(WHISPER_API_KEY_NAME)
    if api_key != WHISPER_API_KEY_VALUE:
        log_msg("Invalid API key")
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_data()

    if len(data) == 0:
        log_msg("No audio file received")
        return jsonify({'error': 'No audio file received'}), 400

    log_msg("Transcribing audio file - starting")

    file_name = 'tmp' + str(random.randint(0, 1000000)) + '.bin'

    with open(file_name, "wb") as file:
        file.write(data)

    try:
        transcription = MODEL.transcribe(audio=file_name)
        log_msg("Transcribing audio file - finished")
        return jsonify({'transcription': transcription['text']}), 200

    except Exception as exception:
        return jsonify({'error': str(exception)}), 500

    finally:
        os.remove(file_name)


def load_config():
    '''Load or generate an API key.'''

    whisper_api_key = None
    model_name = 'medium'

    try:
        with open("config.json", "r", encoding='UTF-8') as config_file:
            config = json.load(config_file)
            whisper_api_key = config.get("whisper_api_key")
            model_name = config.get("model")
    except Exception:
        pass

    if whisper_api_key is None:
        whisper_api_key = str(uuid.uuid4())
        with open("config.json", "w", encoding='UTF-8') as config:
            json.dump({"whisper_api_key": whisper_api_key,
                      "model": model_name}, config)

    return whisper_api_key, model_name


WHISPER_API_KEY_VALUE, model = load_config()
log_msg(f"Whisper API Key: {WHISPER_API_KEY_VALUE}")

MODEL = whisper.load_model(model)

log_msg(f"Model: {model} loaded.")
log_msg("Ready to transcribe audio files.")

if __name__ == '__main__':
    print("main")
    app.run(host='0.0.0.0', port=5500)
