from flask import Flask
from .api import api
from .sms import sms_blueprint
from .login import login_blueprint

def register_blueprints(app: Flask):
    app.register_blueprint(sms_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(api)
