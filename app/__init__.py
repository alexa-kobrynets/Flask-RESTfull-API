import os
from flask import Flask
from peewee import SqliteDatabase
from flask_restful import Api
from flask_bootstrap import Bootstrap
from config import config


bootstrap = Bootstrap()
config_name = os.getenv('FL_CONFIG') or 'default'
db = SqliteDatabase(database=config[config_name].DATABASE)

def create_app(config_name=config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db = SqliteDatabase(config[config_name].DATABASE)
    from .main import main as main_blueprint_app
    app.register_blueprint(main_blueprint_app)
    from .main import blueprint_api
    app.register_blueprint(blueprint_api)
    return app

