'''web front end to the OpenAI Whisper Transcribe service.'''

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import requests

PORT = 8000  # Change this as needed
WHISPER_ENDPOINT = "http://localhost:5500/transcribe"


class MyRequestHandler(SimpleHTTPRequestHandler):
    '''Custom request handler'''

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

        try:
            result = requests.post(
                WHISPER_ENDPOINT, data=file_data, timeout=120)

            if result.status_code == 200:
                result = json.loads(result.text)
                if result:
                    text = (result["transcription"]).strip()

                    print('Transcribing the uploaded file...')

                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(text.encode())
            else:
                self.send_response(result.status_code)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(result.text.encode())

        except Exception as exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(exception))


# Define the server address
server_address = ('', PORT)

# Create an HTTP server with the custom request handler
httpd = HTTPServer(server_address, MyRequestHandler)

# Start the server
print(f'Starting the web server on {PORT}...')

httpd.serve_forever()
