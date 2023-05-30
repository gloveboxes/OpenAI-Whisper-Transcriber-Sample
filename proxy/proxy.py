'''Relay server to forward audio to the transcription server running in WSL 2'''

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    '''Relay server to forward audio to the transcription server running in WSL 2'''
    try:
        # post request to the relay server
        response = requests.post(
            'http://localhost:5500/transcribe', data=request.data, timeout=300)
        return response.text, 200

    except Exception as exception:
        return jsonify({'error': str(exception)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
