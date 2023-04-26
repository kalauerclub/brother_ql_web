from flask import Blueprint

bp = Blueprint('labeldesigner', __name__, template_folder = 'templates')

from . import routes
