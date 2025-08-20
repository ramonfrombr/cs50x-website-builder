from flask import Blueprint

pset2_bp = Blueprint(
    'pset2',
    __name__,
    template_folder='templates',
)

from . import routes