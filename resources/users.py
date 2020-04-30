import models
from flask import Blueprint



users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def test_user_resource(): 
  return "user resource working" 