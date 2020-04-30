import models
from flask import Blueprint, request



users = Blueprint('users', 'users')

# TEST /users
@users.route('/', methods=['GET'])
def test_user_resource(): 
  return "user resource working" 

# REGISTER /users/register
@users.route('/register', methods=['POST'])
def register():
  print(request.get_json())
  return "check terminal" 