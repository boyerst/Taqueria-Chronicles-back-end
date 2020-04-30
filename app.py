from flask import Flask, jsonify



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

  app.run(debug=DEBUG, port=PORT)