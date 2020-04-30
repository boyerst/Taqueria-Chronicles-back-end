from flask import Flask, jsonify

import models


DEBUG=True
PORT=8000


app = Flask(__name__)


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