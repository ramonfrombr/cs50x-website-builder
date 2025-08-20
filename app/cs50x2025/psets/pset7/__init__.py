from flask import Blueprint

pset7_bp = Blueprint(
    'pset7',
    __name__,
    template_folder='templates',
)

from . import routes