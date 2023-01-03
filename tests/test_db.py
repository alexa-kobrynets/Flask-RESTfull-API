from peewee import SqliteDatabase
from app.models import Racing
from flask import current_app
from app import create_app
from config import config


app = create_app('testing')
app_context = app.app_context()
app_context.push()
SqliteDatabase(database=config['testing'].DATABASE)


def test_db():
    assert Racing.select().where(Racing.abbr == 'SVF') == 'SVF'
    assert len(Racing.select()) == 19
    assert current_app.config['TESTING'] == True
    assert current_app is not None





