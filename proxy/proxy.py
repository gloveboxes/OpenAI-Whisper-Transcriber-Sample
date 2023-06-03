'''Relay server to forward audio to the transcription server running in WSL 2'''

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    '''Relay server to forward audio to the transcription server running in WSL 2'''
    try:
        headers = request.headers
        # post request to the relay server
        response = requests.post(
            'http://localhost:5500/transcribe', data=request.data, headers=headers)
        return response.text, response.status_code

    except Exception as exception:
        return jsonify({'error': str(exception)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5600)
