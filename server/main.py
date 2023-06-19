'''This is the main file of the server. It receives the audio file and returns the transcription.'''

import os
import shutil
import random
import datetime as dt
import uuid
import json
import whisper
from fastapi import FastAPI, UploadFile, Response, status, Request
import uvicorn


app = FastAPI()

MODEL = None
WHISPER_API_KEY_VALUE = None
WHISPER_API_KEY_NAME = 'Api-Key'


def log_msg(msg):
    '''Log the request to the console.'''
    print(f"[{dt.datetime.now()}] {msg}")


@app.post("/transcribe", status_code=200)
async def create_upload_file(file: UploadFile, response: Response, request: Request):
    '''Receives the audio file and returns the transcription.'''

    api_key = request.headers.get(WHISPER_API_KEY_NAME)
    if api_key != WHISPER_API_KEY_VALUE:
        log_msg("Invalid API key")
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'error': 'Unauthorized'}

    if file.size == 0:
        log_msg("No audio file received")
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error': 'No audio file received'}

    log_msg(f"Starting: {file.filename} transcription")

    file_name = 'tmp' + str(random.randint(0, 1000000)) + '.bin'

    # copy the file contents
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        transcription = MODEL.transcribe(audio=file_name)
        log_msg(f"Finished: {file.filename} transcription")
        return {'transcription': transcription['text']}

    except Exception as exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'error': str(exception)}, 500

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5500)
