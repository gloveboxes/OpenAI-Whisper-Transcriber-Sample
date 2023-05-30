''' This is the server that will receive the audio file and return the transcription.'''

from flask import Flask, request, jsonify
import whisper
import random
import os
import argparse

app = Flask(__name__)


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    '''Receives the audio file and returns the transcription.'''

    file_name = 'tmp' + str(random.randint(0, 1000000)) + '.bin'

    with open(file_name, "wb") as file:
        file.write(request.data)

    try:
        transcription = model.transcribe(file_name)
        return jsonify({'transcription': transcription['text']}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        os.remove(file_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model")
    args = parser.parse_args()

    # learn more about the models here: https://github.com/openai/whisper/blob/main/model-card.md
    # https://pypi.org/project/openai-whisper/
    
    model = args.model if args.model else "medium"
    model = whisper.load_model(model)

    app.run(host='0.0.0.0', port=5500)
