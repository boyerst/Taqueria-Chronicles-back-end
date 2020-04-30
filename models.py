from peewee import *



DATABASE = SqliteDatabase('users.sqlite')








def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User], safe=True)
  print("Connected to DB and created tables if they weren't already there")

  DATABASE.close()