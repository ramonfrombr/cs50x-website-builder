from flask import Blueprint, render_template

notes_bp = Blueprint(
    'notes',
    __name__,
)

from . import routes
