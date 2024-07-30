from flask import Blueprint

pset6_bp = Blueprint(
    'pset6',
    __name__,
    template_folder='templates',
)

from . import routes