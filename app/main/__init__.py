from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name
from flask.app import Flask
import os

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

# view관련 파일들 경로 설정
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, '../templates/')
STATIC_PATH = os.path.join(APP_PATH, '../static/')


def create_app(config_name: str) -> Flask:
    app = Flask(__name__, template_folder=TEMPLATE_PATH,
                static_folder=STATIC_PATH)

    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
