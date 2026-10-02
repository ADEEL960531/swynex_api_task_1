import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "SWYNEX Backend API")
PORT = int(os.getenv("PORT", 5000))

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": APP_NAME
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SWYNEX Backend API is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
