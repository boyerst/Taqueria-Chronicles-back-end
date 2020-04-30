import models
from flask import Blueprint, request, jsonify



taquerias = Blueprint('taquerias', 'taquerias')


@taquerias.route('/')
def taquerias_index():
  return "taquerias resource working"


# CREATE /taquerias/
@taquerias.route('/', methods=['POST'])
def create_taqueria():
  payload = request.get_json()
  print(payload)
  return "taquerias create route hitting"