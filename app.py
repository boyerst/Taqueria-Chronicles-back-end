from flask import Flask



DEBUG=True
PORT=8000


app = Flask(__name__)


# TEST
@app.route('/')
def say_hello():
  return "Hello"





if __name__ == '__main__':

  app.run(debug=DEBUG, port=PORT)