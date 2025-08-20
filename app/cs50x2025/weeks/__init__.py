from flask import Blueprint

weeks_bp = Blueprint(
    'weeks',
    __name__,
    template_folder='templates'
)

from . import routes
