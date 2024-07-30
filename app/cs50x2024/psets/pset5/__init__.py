from flask import Blueprint

pset5_bp = Blueprint(
    'pset5',
    __name__,
    template_folder='templates',
)

from . import routes