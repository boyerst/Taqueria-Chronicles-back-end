from flask import Flask, jsonify

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


app.register_blueprint(taquerias, url_prefix='/api/v1/taquerias')
app.register_blueprint(users, url_prefix='/api/v1/users')


CORS(taquerias, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

# TEST
@app.route('/')
def say_hello():
  return "Hello"

# TEST JSON
@app.route('/test_json')
def get_json():
  return jsonify(['json', 'functioning'])



if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)