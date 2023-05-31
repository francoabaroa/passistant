from flask import Flask
from app.routes import register_blueprints
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize database and migrate objects
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import the models
    from app.models import User, Family, Reminder, List, ListItem

    # Create the database tables
    with app.app_context():
        db.create_all()

    register_blueprints(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
