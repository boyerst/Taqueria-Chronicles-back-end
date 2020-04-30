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
    'message': f"Here are {len(current_users_taquerias)} taquerias",
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
  taqueria_dict=model_to_dict(new_taqueria)
  print(taqueria_dict)
  taqueria_dict['patron_id'].pop('password')
  return jsonify(
    data=taqueria_dict, 
    message="You have created a Taqueria",
    status=201
  ), 201
  

# DESTROY /taquerias/id
@taquerias.route('/<id>', methods=['DELETE'])
def delete_taqueria(id):
  delete=models.Taqueria.delete().where(models.Taqueria.id == id)
  num_of_rows=delete.execute()
  print(num_of_rows)
  return jsonify(
    data={},
    message="You have deleted {} taqueria with id {}".format(num_of_rows, id),
    status=200
  ), 200



# UPDATE /taquerias/id
@taquerias.route('/<id>', methods=['PUT'])
def update_taqueria(id):
  payload=request.get_json()
  taqueria_to_update=models.Taqueria.get_by_id(id)
  if taqueria_to_update.patron_id.id==current_user.id:
    if 'name' in payload:
      taqueria_to_update.name=payload['name'] 
  
    taqueria_to_update.save()
    updated_taq_dict=model_to_dict(taqueria_to_update)
    updated_taq_dict['patron_id'].pop('password')
    return jsonify(
      data=updated_taq_dict,
      message=f"You have updated the taqueria with id {id}",
      status=200
    ), 200
  else:
    return jsonify(
    data={
      'error': '403 Forbidden'
    },
    message="patron_id does not match taqueria id. You can only edit taquerias that you chronicled.",
    status=403
    ), 403




    taqueria_to_update.save()




