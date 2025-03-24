from flask import Flask, request, jsonify, send_file
from transformers import pipeline
from PIL import Image
import io
import requests

app = Flask(__name__)

# Load the background removal model
pipe = pipeline("image-segmentation", model="briaai/RMBG-2.0", trust_remote_code=True)

@app.route('/')
def home():
    return jsonify({"message": "Background Removal API is running!"})

@app.route('/process-url', methods=['POST'])
def process_url():
    try:
        data = request.get_json()
        image_url = data.get("image_url")

        if not image_url:
            return jsonify({"error": "No image URL provided"}), 400

        # Fetch the image from the URL
        response = requests.get(image_url, stream=True)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch image from URL"}), 400

        # Open image from the URL
        image = Image.open(io.BytesIO(response.content)).convert("RGB")

        # Process the image
        output_image = pipe(image)

        # Convert image to RGBA
        output_image = output_image.convert("RGBA")

        # Save processed image in memory
        img_io = io.BytesIO()
        output_image.save(img_io, format="PNG")
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        print("Error:", str(e))  # Debugging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
