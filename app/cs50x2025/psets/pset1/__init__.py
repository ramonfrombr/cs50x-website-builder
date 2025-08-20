from flask import Blueprint

pset1_bp = Blueprint(
    'pset1',
    __name__,
    template_folder='templates',
)

from . import routes