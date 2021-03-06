import os
from peewee import *
import datetime

from flask_login import UserMixin

from playhouse.db_url import connect


if 'ON_HEROKU' in os.environ: 
  DATABASE = connect(os.environ.get('DATABASE_URL')) 
else:
  DATABASE = SqliteDatabase('taquerias.sqlite')


class User(UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField() 

  class Meta: 
    database=DATABASE

class Taqueria(Model):
  name = CharField()
  patron_id = ForeignKeyField(User, backref='taquerias') 
  address = CharField()                                 
  zip_code = IntegerField()
  rating = IntegerField()
  recommendations = CharField()
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Taqueria], safe=True)
  print("Connected to DB and created tables if they had not existed before")
  DATABASE.close()