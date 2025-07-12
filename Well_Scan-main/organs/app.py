from flask import Flask, request, jsonify
from flask_cors import CORS  # NEW: Enable CORS for frontend
from roboflow import Roboflow
import os

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Initialize Roboflow
rf = Roboflow(api_key="0gzYUtKOKaE5uwnwt66r")
project = rf.workspace("cv-qowsg").project("knee-osteoarthritis-dataset-5mm2n")
model = project.version(1).model

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/classify", methods=["POST"])
def classify_image():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    try:
        # Perform inference with Roboflow
        prediction = model.predict(file_path, confidence=0.5).json()

        # Extract predictions
        predictions = prediction.get("predictions", [])
        if predictions:
            detected_class = predictions[0]["class"]
            confidence = predictions[0]["confidence"] * 100
            result = {"grade": detected_class, "confidence": f"{confidence:.2f}%"}
        else:
            result = {"error": "No predictions found. Try again with a clearer image."}

    except Exception as e:
        result = {"error": f"Inference failed: {str(e)}"}

    finally:
        os.remove(file_path)  # Cleanup uploaded file

    return jsonify(result)

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)