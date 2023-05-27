# Import modules
import os
import http.server
import socketserver
import cgi
import whisper


# Define constants
PORT = 8000 # Change this as needed
UPLOAD_FOLDER = "uploads" # Change this as needed
ALLOWED_EXTENSIONS = set(["mp3", "m4a", "wav"]) # Change this as needed



# Define helper functions
def allowed_file(filename):
    # Check if the file has an allowed extension
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

def save_file(file, filename):
    # Save the file to the upload folder
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, "wb") as f:
        f.write(file)

# Define custom handler class
class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Serve the index.html file for the root path
        if self.path == "/":
            self.path = "/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        # Handle file upload requests
        if self.path == "/upload":
            content_length = int(self.headers['Content-Length'])
        
            # Read the request body
            post_data = self.rfile.read(content_length)

            # Parse the form data
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={"REQUEST_METHOD": "POST"}
            )
            # Get the file field
            file_field = form["file"]
            # Check if the file field is valid
            if file_field.filename and allowed_file(file_field.filename):
                # Save the file
                save_file(file_field.file.read(), 'temp.bin')
                # Send a success response
                transcription = model.transcribe(os.path.join('uploads', 'temp.bin'))
                self.send_response(200, transcription['text'])
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(transcription['text'].encode())
            else:
                # Send an error response
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Invalid file")
            os.remove(os.path.join('uploads', 'temp.bin'))
        else:
            # Send a not found response for other paths
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not found")

# Create a server object
server = socketserver.TCPServer(("", PORT), CustomHandler)

# learn more about the models here: https://pypi.org/project/openai-whisper/
model = whisper.load_model("large")

# Start the server
print(f"Serving at port {PORT}")
server.serve_forever()
