# Background Removal API

This project provides a Flask-based API to remove backgrounds from images using the `briaai/RMBG-1.4` model.

## 🚀 Features
- Removes backgrounds from images via a URL.
- Uses `transformers` pipeline for image segmentation.
- Returns the processed image in **PNG format**.

## 🛠️ Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/vidula-20/background_api_removal_briaai-RMBG-2.0

2. Install dependencies:
   pip install -r requirements.txt

3. Run the API
   python app.py

4. Send a Request
Use Postman or curl:

curl -X POST "http://127.0.0.1:5000/process-url" \
     -H "Content-Type: application/json" \
     -d '{"image_url": "https://example.com/sample.jpg"}'
