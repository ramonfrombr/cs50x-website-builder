from flask import Blueprint

pset9_bp = Blueprint(
    'pset9',
    __name__,
    template_folder='templates',
)

from . import routes