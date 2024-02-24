from flask import Blueprint, render_template

psets_bp = Blueprint(
    'psets',
    __name__,
)

from . import routes
