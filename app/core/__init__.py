from flask import Blueprint
from .manual import manual_bp

core = Blueprint(
    'core',
    __name__,
    template_folder='templates'
)

core.register_blueprint(
    manual_bp, url_prefix=f"/manual")

from . import routes
