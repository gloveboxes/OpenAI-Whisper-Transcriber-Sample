''' This is the server that will receive the audio file and return the transcription.'''

import random
import os
import argparse
import json
import uuid
import whisper
from flask import Flask, request, jsonify

app = Flask(__name__)
WHISPER_API_KEY_VALUE = None
WHISPER_API_KEY_NAME = 'Api-Key'
MODEL = None


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    '''Receives the audio file and returns the transcription.'''

    # check if the whisper api key is valid
    api_key = request.headers.get(WHISPER_API_KEY_NAME)
    if api_key != WHISPER_API_KEY_VALUE:
        return jsonify({'error': 'Unauthorized'}), 401

    file_name = 'tmp' + str(random.randint(0, 1000000)) + '.bin'

    with open(file_name, "wb") as file:
        file.write(request.data)

    try:
        transcription = MODEL.transcribe(file_name)
        return jsonify({'transcription': transcription['text']}), 200

    except Exception as exception:
        return jsonify({'error': str(exception)}), 500

    finally:
        os.remove(file_name)

def load_api_key():
    '''Load or generate an API key.'''

    try:
        with open("config.json", "r", encoding='UTF-8') as config_file:
            whisper_api_key = json.load(config_file)["whisper_api_key"]
    except Exception:
        whisper_api_key = str(uuid.uuid4())
        with open("config.json", "w", encoding='UTF-8') as config:
            json.dump({"whisper_api_key": whisper_api_key}, config)

    return whisper_api_key

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model")
    args = parser.parse_args()

    WHISPER_API_KEY_VALUE = load_api_key()
    print(f"Whisper API Key: {WHISPER_API_KEY_VALUE}")

    # learn more about the models here: https://github.com/openai/whisper/blob/main/model-card.md
    # https://pypi.org/project/openai-whisper/

    model_name = args.model if args.model else "medium"
    MODEL = whisper.load_model(model_name)

    app.run(host='0.0.0.0', port=5500)
