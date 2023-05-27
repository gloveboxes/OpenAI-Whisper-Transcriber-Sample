from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import whisper


# learn more about the models here: https://pypi.org/project/openai-whisper/
WHISPER_MODEL = "large"  # Change this as needed

UPLOAD_FOLDER = "uploads"  # Change this as needed
PORT = 8000  # Change this as needed


class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        '''Serves the index.html file for the root path.'''

        if self.path == "/":
            self.path = "/index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        '''Handles file upload request and calling the OpenAI Whisper Transcribe.'''
        content_length = int(self.headers['Content-Length'])

        # Read the request body
        post_data = self.rfile.read(content_length)

        # Extract the file data
        file_start = post_data.find(b'\r\n\r\n') + 4
        file_data = post_data[file_start:]

        filepath = os.path.join(UPLOAD_FOLDER, 'temp.bin')

        try:
            with open(filepath, "wb") as f:
                f.write(file_data)

            print('Transcribing the uploaded file...')
            transcription = model.transcribe(filepath)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(transcription['text'].encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(e))

        finally:
            os.remove(filepath)


print(f'Loading the OpenAI Whisper "{WHISPER_MODEL}" model...')
model = whisper.load_model(WHISPER_MODEL)

# Define the server address
server_address = ('', PORT)

# Create an HTTP server with the custom request handler
httpd = HTTPServer(server_address, MyRequestHandler)

# Start the server
print(f'Starting the web server on {PORT}...')

httpd.serve_forever()
