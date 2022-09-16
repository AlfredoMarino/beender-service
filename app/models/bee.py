import peewee

from app.core.db import db
from app.models.base_model import BaseModel


# class Bee(BaseModel):
class Bee(peewee.Model):
    firstname = peewee.CharField()
    lastname = peewee.CharField()
    interested_in = peewee.CharField()
    experience_years = peewee.IntegerField()
    picture = peewee.CharField()
    bio = peewee.CharField()

    class Meta:
        database = db
