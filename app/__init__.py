from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_migrate import Migrate
# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    # existing code remains
    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app