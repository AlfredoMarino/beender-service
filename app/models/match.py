from peewee import ForeignKeyField, BooleanField, IntegerField

from app.models.base_model import BaseModel
from app.models.hive import Hive


class Match(BaseModel):
    hive_id = ForeignKeyField(Hive, backref="match")
    bee_id = IntegerField()
    beeAccept = BooleanField()
    hiveAccept = BooleanField()
