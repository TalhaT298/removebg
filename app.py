from flask import Flask, request, render_template, send_file
from PIL import Image
from rembg import remove
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    # Remove background
    # Remove background
    # Remove background
    # Remove background
    # Remove background
    # Remove background
    # Remove background# 
    input_image = Image.open(file)
    output_image = remove(input_image)

    output_path = 'static/removed_background.png'
    output_image.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
