from flask import Blueprint, jsonify

example = Blueprint('example', __name__)

@example.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})
