from flask import Blueprint

pset8_bp = Blueprint(
    'pset8',
    __name__,
    template_folder='templates',
)

from . import routes