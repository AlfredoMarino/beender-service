from peewee import CharField

from app.models.base_model import BaseModel


class Hive(BaseModel):
    name = CharField()
    description = CharField()
    queen_bee = CharField()
    picture = CharField()
