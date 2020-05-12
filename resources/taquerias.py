import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required


taquerias = Blueprint('taquerias', 'taquerias')

# INDEX /taquerias
@taquerias.route('/', methods=['GET'])
# @login_required
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
@login_required
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
@login_required
def delete_taqueria(id):
  try:
    taq_to_delete=models.Taqueria.get_by_id(id)
    if taq_to_delete.patron_id.id==current_user.id:
      taq_to_delete.delete_instance()
      return jsonify(
        data={},
        message=f"You have deleted the Taqueria with id {id}",
        status=200
      ), 200
    else: 
      return jsonify(
      data={
        'error': '403 Forbidden'
      },
      message="You do not have permission to delete this Taqueria.",
      status=403
      ), 403
  except models.DoesNotExist:
    return jsonify(
      data={
        'error': '404 Not found'
      },
      message="There is no Taqueria with that ID.",
      status=404
    ), 404



# UPDATE /taquerias/id
@taquerias.route('/<id>', methods=['PUT'])
@login_required
def update_taqueria(id):
  payload=request.get_json()
  taqueria_to_update=models.Taqueria.get_by_id(id)
  if taqueria_to_update.patron_id.id==current_user.id:
    if 'name' in payload:
      taqueria_to_update.name=payload['name'] 
    if 'address' in payload:
      taqueria_to_update.address=payload['address']
    if 'zip_code' in payload:
      taqueria_to_update.zip_code=payload['zip_code']
    if 'rating' in payload:
      taqueria_to_update.rating=payload['rating']
    if 'recommendations' in payload:
      taqueria_to_update.recommendations=payload['recommendations']
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


# SHOW /taquerias/id
@taquerias.route('/<id>', methods=['GET'])
def show_taqueria(id):
  taqueria=models.Taqueria.get_by_id(id)
  if not current_user.is_authenticated:
    return jsonify(
      data={
        'name': taqueria.name,
        'address': taqueria.address,
        'zip_code': taqueria.zip_code,
        'rating': taqueria.rating,
        'recommendations': taqueria.recommendations
      },
      message="Here is the taqueria",
      status=200
    ), 200
  else:
    taqueria_dict=model_to_dict(taqueria)
    taqueria_dict['patron_id'].pop('password')
    return jsonify(
      data=taqueria_dict,
      message=f"Here is a closer look at taqueria {id}",
      status=200
    ), 200


