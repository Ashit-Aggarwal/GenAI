from flask import Flask, request, jsonify
from image_utils import generate_image

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    image_path = generate_image(prompt)
    return jsonify({"image_url": image_path})
