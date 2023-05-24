from flask import Flask
from .example import example

def register_blueprints(app: Flask):
    app.register_blueprint(example)
