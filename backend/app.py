from flask import Flask
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)