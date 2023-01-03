from peewee import *
from app import db


class Racing(Model):
    id = PrimaryKeyField(unique=True)
    abbr = CharField()
    name = CharField()
    team = CharField()
    time = DateTimeField()

    class Meta:
        database = db
        order_by = 'place'
        db_table = 'teams_result'
