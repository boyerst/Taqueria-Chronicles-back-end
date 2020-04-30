import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

from flask_login import current_user


taquerias = Blueprint('taquerias', 'taquerias')

# INDEX /taquerias
@taquerias.route('/', methods=['GET'])
def taquerias_index():
  current_users_taquerias=[model_to_dict(taqueria) for taqueria in current_user.taquerias]
  for taqueria_dict in current_users_taquerias:
    taqueria_dict['patron_id'].pop('password')
  print(current_users_taquerias)
  return jsonify({
    'data': current_users_taquerias,
    'message': f"Here are {len(current_users_taquerias)}",
    'status': 200
  }), 200
  


# CREATE /taquerias/
@taquerias.route('/', methods=['POST'])
def create_taqueria():
  payload=request.get_json()
  print(payload)
  new_taqueria=models.Taqueria.create(
    name=payload['name'],
    patron_id=current_user.id,
    address=payload['address'],
    zip_code=payload['zip_code'],
    rating=payload['rating'],
    recommendations=payload['recommendations']
  )
  taqueria_dict = model_to_dict(new_taqueria)
  print(taqueria_dict)
  taqueria_dict['patron_id'].pop('password')
  return jsonify(
    data=taqueria_dict, 
    message="You have created a Taqueria",
    status=201
  ), 201
  