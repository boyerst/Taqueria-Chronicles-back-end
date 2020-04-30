from peewee import *



DATABASE = SqliteDatabase('taquerias.sqlite')



class User(Model):
  username=CharField(unique=True)
  email=CharField(unique=True)
  password=CharField() 

  class Meta: 
    database=DATABASE




def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User], safe=True)
  print("Connected to DB and created tables if they weren't already there")

  DATABASE.close()