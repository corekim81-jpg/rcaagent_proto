from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/version")
def version():
    return jsonify({"version": "0.1.0"})
