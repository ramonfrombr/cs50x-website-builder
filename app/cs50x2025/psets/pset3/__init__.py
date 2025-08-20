from flask import Blueprint

pset3_bp = Blueprint(
    'pset3',
    __name__,
    template_folder='templates',
)

from . import routes