from flask import Blueprint

pset0_bp = Blueprint(
    'pset0',
    __name__,
    template_folder='templates',
)

from . import routes