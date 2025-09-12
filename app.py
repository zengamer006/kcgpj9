from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    secret_value = os.environ.get("MY_SECRET", "No secret configured")
    return jsonify({
        "message": "Hello, Flask API is working!",
        "secret": secret_value
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
