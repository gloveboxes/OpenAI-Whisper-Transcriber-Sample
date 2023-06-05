# Running OpenAI Whisper Sample

The full documentation for this project is published [here](https://gloveboxes.github.io/OpenAI-Whisper-Transcriber-Docs/).

## Solution overview

OpenAI Whisper is a speech-to-text transcription library that uses the [OpenAI Whisper](https://openai.com/research/whisper) models. 

Welcome to the OpenAI Whisper Transcriber Sample. This sample demonstrates how to use the [openai-whisper](https://pypi.org/project/openai-whisper/) library to transcribe audio files. 

Follow the deployment and run instructions on the right hand side of this page to deploy the sample.

## What is OpenAI Whisper?

The OpenAI Whisper model is an Open Source speech-to-text transcription model that is trained on 680,000 hours of multilingual and multitask supervised data collected from the web. 

OpenAI describes Whisper as an[encoder-decoder transformer](https://kikaben.com/transformers-encoder-decoder/), a type of neural network that can use context gleaned from input data to learn associations that can then be translated into the model's output.

## Solution Architecture

The solution is divided into two parts:

1. A Whisper service, that wraps the [openai-whisper](https://pypi.org/project/openai-whisper/) library and loads the Whisper model and exposes the model as a REST API.
2. A Whisper client, that calls the Whisper service to transcribe audio files. There are two clients:
    1. A GUI client that runs on Windows, macOS, and Linux.
    2. A Web client.

The advantage of this architecture is the model is loaded once by the Whisper service, a relatively time consuming process, and called multiple times by the Whisper clients.

![media/architecture.png](https://github.com/gloveboxes/OpenAI-Whisper-Transcriber-Sample/wiki/media/architecture.png)
