from flask import Flask
from flask import g
from flask import jsonify
import os
from flask import make_response, Response
from resources.taquerias import taquerias
from resources.users import users

import models

from flask_cors import CORS

from flask_login import LoginManager


DEBUG=True
PORT=8000



app = Flask(__name__)


app.secret_key = "secret time"
login_manager = LoginManager()
login_manager.init_app(app)

print("secret keyAEWTERGEWRGEWRGE EWRGERTGEWRGEGHERht")
print(app.secret_key)


# USER LOADER
@login_manager.user_loader
def load_user(user_id):
  try:
    print("loading the following user")
    user = models.User.get_by_id(user_id)
    return user 
  except models.DoesNotExist: 
    return None

# LOGIN MANAGER
@login_manager.unauthorized_handler
def unauthorized():
  return jsonify (
    data={
      'error': 'The user is not logged in'
    },
    message='Forget to login? Please do so - or register u are new to the Chronicles',
    status=401
  ), 401




CORS(users, origins=['http://localhost:3000', 'https://taquerias-react.herokuapp.com'], supports_credentials=True)
CORS(taquerias, origins=['http://localhost:3000', 'https://taquerias-react.herokuapp.com'], supports_credentials=True)

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(taquerias, url_prefix='/api/v1/taquerias')


@app.before_request 
def before_request():
  print("you should see this before each request") 
  g.db = models.DATABASE
  g.db.connect()

@app.after_request 
def after_request(response):
  print("you should see this after each request") 
  g.db.close()
  return response 
            



# # TEST
# @app.route('/')
# def say_hello():
#   return "Hello"

# # TEST JSON
# @app.route('/test_json')
# def get_json():
#   return jsonify(['json', 'functioning'])





if 'ON_HEROKU' in os.environ: 
  print('\non heroku!')
  models.initialize()

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)