''' This is the server that will receive the audio file and return the transcription.'''

from flask import Flask, request, jsonify
import whisper
import random
import os

app = Flask(__name__)

# learn more about the models here: https://pypi.org/project/openai-whisper/
model = whisper.load_model("large")


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
    app.run(host='0.0.0.0')
