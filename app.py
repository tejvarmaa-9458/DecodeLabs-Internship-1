from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def index():
    return send_file(BASE_DIR / "index.html")


@app.get("/index.js")
def index_js():
    return send_file(BASE_DIR / "index.js")


@app.post("/start-interview")
def start_interview():
    payload = request.get_json(silent=True) or {}
    subject = payload.get("subject", "General")
    question = f"Please introduce yourself and share your experience in {subject}."
    return jsonify({"question": question})


@app.post("/submit-answer")
def submit_answer():
    if "audio" not in request.files:
        return jsonify({"error": "No audio uploaded."}), 400

    audio_file = request.files["audio"]
    if audio_file.filename == "":
        return jsonify({"error": "No selected audio file."}), 400

    saved_path = UPLOAD_DIR / audio_file.filename
    audio_file.save(saved_path)

    return jsonify({
        "success": True,
        "message": "Answer received successfully.",
        "next_question": "Tell me about one project you are proud of."
    })


@app.post("/get-feedback")
def get_feedback():
    return jsonify({
        "success": True,
        "feedback": {
            "subject": "Python",
            "candidate_score": 4.5,
            "feedback": "You explained your ideas clearly and stayed relevant to the topic.",
            "areas_of_improvement": "Try speaking a little more confidently and give a few more practical examples."
        }
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
