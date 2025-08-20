from flask import Blueprint

pset4_bp = Blueprint(
    'pset4',
    __name__,
    template_folder='templates',
)

from . import routes