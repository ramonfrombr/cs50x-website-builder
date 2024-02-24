from flask import Blueprint, render_template

weeks_bp = Blueprint(
    'weeks',
    __name__,
)

from . import routes
