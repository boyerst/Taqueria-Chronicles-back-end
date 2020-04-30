import models
from flask import Blueprint



taquerias = Blueprint('taquerias', 'taquerias')


@taquerias.route('/')
def taquerias_index():
  return "taquerias resource working"


# CREATE /taquerias/
@taquerias.route('/', methods=['POST'])
def create_taqueria():
  return "taquerias create route hitting"