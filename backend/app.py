from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Nebula FX Backend Running 🚀"}

@app.route("/fx-rate")
def get_fx_rate():
    # Demo API (we will replace later with real one)
    url = "https://api.exchangerate.host/latest?base=USD&symbols=INR"

    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
