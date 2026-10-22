
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/api/events")
def events():
    return jsonify([])

@app.route("/api/accounts")
def accounts():
    return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
