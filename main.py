from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        image = Image.open(file.stream)
        image.thumbnail((300, 300))  # Resize the image to fit in a 300x300 box
        image_io = io.BytesIO()
        image.save(image_io, 'JPEG')
        image_io.seek(0)
        return send_file(image_io, mimetype='image/jpeg')

@app.route('/resize', methods=['POST'])
def resize():
    width = int(request.form.get('width', 0))
    height = int(request.form.get('height', 0))
    if width <= 0 or height <= 0:
        return 'Width and height must be greater than 0.'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        image = Image.open(file.stream)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_io = io.BytesIO()
        image.save(image_io, 'JPEG')
        image_io.seek(0)
        return send_file(image_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
