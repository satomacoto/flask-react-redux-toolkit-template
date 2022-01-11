from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return jsonify({"hello": "world"})
