from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config
import random
import secrets
import os
from app.models import create_sample_data
from dotenv import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


migrate = Migrate()


@app.context_processor
def inject_project_name():
    return dict(projectName=os.environ.get("PROJECT_NAME", "Default Flask App"))


# generating a random token number
def gen_token():
    _TOKEN = secrets.token_hex(16)
    token = "".join(random.choice(_TOKEN) for _ in range(32))

    file_path = "app/config.py"


    with open(file_path, "r") as file:
        content = file.read()

    content = content.replace("SECRET_KEY_TOKEN", token)

    with open(file_path, "w") as file:
        file.write(content)

def create_app(config_name):
    gen_token()
    app.config.from_object(config[config_name])
    from app.models import db
    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import models to ensure database tables are created
        from . import models
        from . import views

        # Initialize the database
        db.create_all()
        create_sample_data()

    return app
