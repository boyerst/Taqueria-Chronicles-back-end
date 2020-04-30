import models
from flask import Blueprint, request, jsonify
from flask_login import current_user


taquerias = Blueprint('taquerias', 'taquerias')


@taquerias.route('/')
def taquerias_index():
  return "taquerias resource working"


# CREATE /taquerias/
@taquerias.route('/', methods=['POST'])
def create_taqueria():
  payload = request.get_json()
  print(payload)
  new_taqueria = models.Taqueria.create(
    name=payload['name'],
    patron_id=current_user.id,
    address=payload['address'],
    zip_code=payload['zip_code'],
    rating=payload['rating'],
    recommendations=payload['recommendations']
  )
  return "taquerias create route hitting"