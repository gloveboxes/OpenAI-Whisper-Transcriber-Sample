# Running OpenAI Whisper Sample

This OpenAI Whisper sample loads the Whisper models using a Flask app. The advantage of loading up with Flask is the model is loaded once. Importing the `whisper` library and loading the Whisper model are relatively slow, but once loaded by the Flask app the model can be called multiple times without reloading the `whisper` library and model.

Note, the Flask app is not thread safe, so, you can't send multiple audio files to be transcribed by the Flask server at the same time.

## Windows installation

### Recommended setup

1. See the `Setup` section of the [OpenAI Whisper Project Description](https://pypi.org/project/openai-whisper/) page.
1. At the time of writing, May 2023, I used Python 3.11.3 and PyTorch 11.7 and the project worked as expected.

## Installing the GUI client perquisites

To run the OpenAI Whisper Client app, you need to install the required Python Libraries and Tkinker.

### Install the Python Client libraries

1. From the command line, navigate to the `client` folder.
2. Run the following command to install the required Python libraries.
   
   ```bash
   pip3 install -r requirements.txt
   ```

### Installing Tkinker on Linux

```bash
apt-get install python-tk
```

### Installing Tkinker on macOS

```bash
brew install python-tk
```


### Install prerequisites

1. Install Miniconda
2. Create a conda environment.

    ```bash
    conda create -n whisper python=3.11.3
    ```
3. Activate the conda environment

    ```bash
    conda activate whisper
    ```
4. Install [openai-whisper](https://pypi.org/project/openai-whisper/)

    ```bash
    pip install openai-whisper chardet flask requests
    ```

### Install CUDA/GPU accelerated version of PyTorch

If you are running in Windows or Linux and you have an NVidia GPU then

1. Uninstall the version of torch installed when you installed openai-whisper. By default, openai-whisper library installs the CPU version of the PyTorch.
2. Follow the instructions to install `torch` with CUDA/GPU support, see installing [Pytorch](https://pytorch.org/get-started/locally/). At the time of writing, the Conda install command for the CUDA/GPU version of PyTorch is:

    ```bash
    conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
    ```

### Install FFmpeg

1. You can download the [latest release](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip) from [FFmpeg-Builds](https://github.com/BtbN/FFmpeg-Builds/releases).
2. Unzip the downloaded FFmpeg file, move to your preferred app folder.
3. From `System Properties`, select `Environment Variables`, and add the path to the FFmpeg bin folder to the path.
4. Close existing `Terminal` windows, open a new `Terminal` window to load the updated environment path. Run the following command to test the installation of FFmpeg.

    ```bash
    ffmpeg -version
    ```

## Run the OpenAI Whisper Flask Server

By default, the Flask server with load the `large` OpenAI Whisper model. This fine if you have 10 to 12 GB of VRAM on your graphics card. See the `Available models and languages` section of the [OpenAI Whisper Project Description](https://pypi.org/project/openai-whisper/).

From VS Code or the command line, run

```bash
pythons server.py
```

Make a note of the IP addresses and the port number the server starts on. For example:

```text
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5500
 * Running on http://192.168.1.83:5500
```

## Send an audio file to the Flask Server

The easiest way is with [Postman](https://www.postman.com/).

1. Create a new HTTP request
2. Select `POST`
3. Enter the endpoint of your flask server. Eg, `http://127.0.0.1:5500/transcribe`
4. Select `Body`, then select `binary`
5. Select the audio file you wish to transcribe
6. Select `Send`

![The image is a screenshot of Postman for sending an audio file](media/postman.png)

The audio file will be transcribed and when complete, will return a JSON document with the transcription. Here's an example of a transcription that was a mix of English questions with Tagalog replies.

```json
{
    "transcription": " Hi, so how was the gym today? Mabuti. Madaming tao. So what did you do? Ginamit ko yung treadmill. Did you do any stretching? Hindi. Not today? Hindi ngayong araw."
}
```
