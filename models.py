from peewee import *
import datetime


DATABASE = SqliteDatabase('taquerias.sqlite')



class User(Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField() 

  class Meta: 
    database=DATABASE

class Taqueria(Model):
  name = CharField()
  patron_id = IntegerField()
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
  print("Connected to DB and created tables if they weren't already there")

  DATABASE.close()