import models
from flask import Blueprint



taquerias = Blueprint('taquerias', 'taquerias')


@taquerias.route('/')
def taquerias_index():
  return "taquerias resource working"