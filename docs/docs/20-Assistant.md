# Home Assistant

## Requirements

## Cloud Services

The Home Assistant uses the following cloud services:

1. [OpenAI](https://platform.openai.com) chat and depending on your configuration, the `Whisper` speech to text transcriber.
2. The [Weather API](https://www.weatherapi.com/) to get weather data.

### OpenAI API

This project uses the [OpenAI Chat Completion API](https://platform.openai.com/docs/api-reference/chat) to extract OpenAI Functions and generate text.

Create an OpenAI account and get an API key.

1. Sign up for an OpenAI account at https://platform.openai.com.
2. Create an API key at https://platform.openai.com/account/api-keys.

Save the API key in the `OPENAI_API_KEY` environment variable.

### Weather API

This project uses the [Weather API](https://www.weatherapi.com/) to get weather data. This data is used to `ground` the GPT prompts the assistant generates.

Create a Weather API account and get an API key.

1. Sign up for a [Weather API account](https://www.weatherapi.com/signup.aspx).
2. Create a free [Weather API key](https://www.weatherapi.com/my/).
3. Save the API key in the `WEATHER_API_KEY` environment variable.

## Clone the repository

```bash
git clone https://github.com/gloveboxes/OpenAI-Whisper-Transcriber-Sample
```

## Install prerequisites

1. Install Python version 3.8 ~ 3.10. The [Whisper library](https://pypi.org/project/openai-whisper/) is supported on Python 3.8 to 3.10.
1. Install the required Python packages:
1. Create a Python virtual environment:

    ```bash
    python -m venv .assistant
    ```

1. Activate the Python virtual environment:

    Windows

    ```pwsh
    ./.assistant/Scripts/activate
    ```

    Linux and macOS

    ```bash
    source .assistant/bin/activate
    ```

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

1. On Windows, by default, the `requirements.txt` file will install the CPU version of PyTorch. If you have an NVidia GPU, you can install the CUDA accelerated version of PyTorch.

    1. First uninstall the CPU version of PyTorch:

        ```pwsh
        pip3 uninstall torch torchvision torchaudio
        ```

    2. Install the CUDA accelerated version of PyTorch:

        Review the [PyTorch website](https://pytorch.org/get-started/locally/) for the latest installation instructions.

        ```bash
        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
        ```

### Set the Text to Speech Transcriber mode

There are three modes to use Whisper speech to text transcriber:

1. `local`: The Whisper speech to text transcription is done locally on the device. This is the default mode and free mode. The speed will depend on the hardware capabilities of your computer. The first time the Whisper speech to text transcriber is used, it will download the transcriber model from the internet. This will take a few minutes.
2. `openai`: The Whisper speech to text transcription is done using the OpenAI API. This is a paid service, review [OpenAI Audio Model Pricing](https://openai.com/pricing/) for more information.
3. `gpu`: You can run your own Whisper services on your own NVidia GPU. Depending on your GPU configuration, this can be a lot faster than the `local` mode.

### Installing prerequisites



## Run