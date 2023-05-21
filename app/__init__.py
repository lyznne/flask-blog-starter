from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):

    app.config.from_object(config[config_name])

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to ensure database tables are created
    from . import models

    # Import views or blueprints
    from . import views

    with app.app_context():
    # Initialize the database
        db.create_all()
    

    return app
