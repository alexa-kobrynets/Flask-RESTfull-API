import os
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_ADMIN = os.environ.get('FL_ADMIN')
    PATH_DATA = Path(__file__).absolute().parent / 'data'
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = Path(__file__).absolute().parents[0] / 'data' / 'racers.db'


class TestingConfig(Config):
    TESTING = True
    DATABASE = Path(__file__).absolute().parents[0] / 'tests' / 'test_db.db'


class ProductionConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
