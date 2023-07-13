---
sidebar_position: 0
slug: /
---

import Social from '@site/src/components/social';

<Social
    page_url="https://gloveboxes.github.io/OpenAI-Whisper-Transcriber-Sample"
    image_url="https://gloveboxes.github.io/OpenAI-Whisper-Transcriber-Sample/assets/images/whispering-wide-66e027604c6c49af3c4a05b6144b2f40.jpeg"
    title="OpenAI Whisper Transcriber"
    description= "🏭 Get started with OpenAI Whisper Speech to Text Transcription"
    hashtags="OpenAI"
    hashtag=""
/>

![](../static/img/whispering-wide.jpeg)

# Build a home assistant with OpenAI Whisper and Functions

This sample demonstrates how you can build a simple home assistant with [OpenAI Whisper](https://openai.com/research/whisper) and [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling). OpenAI Whisper is a powerful multilingual speech-to-text transcription model. OpenAI Functions extract structured data from unstructured prompt data, making it easier for your code to determine the next course of action.

## What is OpenAI Whisper?

The OpenAI Whisper model is an Open Source speech-to-text transcription model that is trained on 680,000 hours of multilingual and multitask supervised data collected from the web. The whisper model is available as a cloud [Speech to text API](https://platform.openai.com/docs/guides/speech-to-text) from OpenAI or you can run the Whisper model locally. This sample demonstrates how to run the Whisper model locally with the [openai-whisper](https://pypi.org/project/openai-whisper/) library to transcribe audio files.

<!-- OpenAI describes Whisper as an [encoder-decoder transformer](https://kikaben.com/transformers-encoder-decoder/), a type of neural network that can use context gleaned from input data to learn associations that can then be translated into the model's output. Quote from the [OpenAI Whisper](https://openai.com/research/whisper) webpage:

> We’ve trained and are open-sourcing a neural net called Whisper that approaches human level robustness and accuracy on English speech recognition. Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English. We are open-sourcing models and inference code to serve as a foundation for building useful applications and for further research on robust speech processing. -->

## What are OpenAI Functions

OpenAI Function enables you to describe functions to gpt-3.5-turbo-0613 and gpt-4-0613 models and later, and have the GPT model intelligently select which function (if any) best matches the data in the prompt. The function definitions along with the prompt are passed to the OpenAI Chat Completion API. The GPT model then determines which function best matches the prompt and populates a JSON object using the function JSON schema and prompt data. If there is a successful match, the chat completion API returns the function name and the JSON object/entity.


## Running OpenAI Whisper Sample

The Whisper model runs best on an NVidia GPU from WSL2 or Linux. The sample code will run on a CPU, both Intel and Apple Silicon are supported, but transcription will be slower. If you are running the model on a CPU then it's recommended to use smaller Whisper models for the transcriptions.

## Solution Architecture

The solution is divided into two parts:

1. A Whisper service, that wraps the [openai-whisper](https://pypi.org/project/openai-whisper/) library and loads the Whisper model, and exposes the model as a REST API.
2. A Whisper client, that calls the Whisper service to transcribe audio files. There are two clients:
    1. A GUI client that runs on Windows, macOS, and Linux.
    2. A Web client.

The advantage of this architecture is the model is loaded once by the Whisper service, a relatively time-consuming process, and then called multiple times by the Whisper clients.

![](media/architecture.png)
