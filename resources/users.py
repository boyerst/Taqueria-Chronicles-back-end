import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash

from playhouse.shortcuts import model_to_dict

from flask_login import login_user


users = Blueprint('users', 'users')

# TEST /users
@users.route('/', methods=['GET'])
def test_user_resource(): 
  return "user resource working" 


# REGISTER /users/register
@users.route('/register', methods=['POST'])
def register():
  payload = request.get_json()
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
    login_user(created_user) #NOTE: takes user OBJ and logs them in/starts session
    created_user_dict = model_to_dict(created_user)
    print(type(created_user_dict['password']))
    created_user_dict.pop('password')

    return jsonify(
        data=created_user_dict,
        message=f"Welcome {created_user_dict['username']}! We are looking forward to your additions to Chicago's own Taqueria Chronicles",
        status=201
      ), 201


# LOGIN /users/login
@users.route('/login', methods=['POST'])
def login():
  payload = request.get_json()
  payload['email'] = payload['email'].lower()
  payload['username'] = payload['username'].lower()
  try: 
    user = models.User.get(models.User.email == payload['email'])
    user_dict = model_to_dict(user)
    matching_password = check_password_hash(user_dict['password'], payload['password'])
    if(matching_password):
      login_user(user) 
      print(model_to_dict(user))
      user_dict.pop('password')
      return jsonify(
        data=user_dict,
        message=f"Welcome back {user_dict['username']}! You have successfully logged in.",
        status=200
      ), 200
    else:
      print("Password does not match")
      return jsonify(
        data={},
        message="Please try again. If you have not already registered, please do so", 
        status=401
      ), 401
  except models.DoesNotExist:
    print('not today')


  return "check terminal"






