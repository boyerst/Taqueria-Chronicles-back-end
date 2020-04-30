from flask import Flask, jsonify

from resources.taquerias import taquerias

import models

from flask_cors import CORS

from flask_login import LoginManager


DEBUG=True
PORT=8000


app = Flask(__name__)


app.register_blueprint(taquerias, url_prefix='/api/v1/taquerias')

CORS(taquerias, origins=['http://localhost:3000'], supports_credentials=True)

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