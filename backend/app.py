from flask import Flask
from app.routes import register_blueprints
from app import db
from config import Config
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import Member, Family, Reminder, List, ListItem

    with app.app_context():
        db.create_all()

    register_blueprints(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
