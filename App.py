from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "SWYNEX Backend API"
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "SWYNEX Backend API is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
