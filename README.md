# Background Remover Application

This is a simple **Flask web application** for removing backgrounds from uploaded images. Built with Flask, Python's Pillow library, and the Rembg package, this application allows users to upload an image, removes its background, and provides the processed image for download..

## Features

- **Background Removal**: Uses Rembg to process images and remove backgrounds efficiently.
- **User-Friendly Interface**: Tailwind CSS provides a clean and responsive UI.
- **File Upload and Download**: Users can upload an image and download the background-removed version.

## Technologies Used

- **Backend**: Flask, Rembg, PIL (Python Imaging Library)
- **Frontend**: HTML, Tailwind CSS for styling

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/background-remover.git
    cd background-remover
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    python app.py
    ```

4. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage

1. Navigate to the application homepage.
2. Upload an image file by selecting it from your device.
3. Click **Remove Background** to process the image.
4. The processed image will be available for download.

---

