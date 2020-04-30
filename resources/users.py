import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash



users = Blueprint('users', 'users')

# TEST /users
@users.route('/', methods=['GET'])
def test_user_resource(): 
  return "user resource working" 


# REGISTER /users/register
@users.route('/register', methods=['POST'])
def register():
  payload = request.get_json()
  # print(payload)
  payload['username'] = payload['username'].lower()
  payload['email'] = payload['email'].lower()
  print(payload)

  try:
    models.User.get(models.User.email == payload['email'])
    return jsonify(
      data={},
      message=f"Sorry, a user with the email {payload['email']} already exists",
      status=401
    ), 401


  except models.DoesNotExist:
    created_user = models.User.create(
      username=payload['username'],
      email=payload['email'],
      password=generate_password_hash(payload['password'])
    )
    print(created_user)


  
  return "check terminal"