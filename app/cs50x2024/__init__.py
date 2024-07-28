from flask import Blueprint

cs50x2024 = Blueprint(
    'cs50x2024',
    __name__,
    template_folder='templates'
)

from . import routes
