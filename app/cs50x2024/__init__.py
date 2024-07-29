import os
from flask import Blueprint
from .weeks import weeks_bp
from .notes import notes_bp
from .content.english.language import pages_url as english_pages_url
from .content.spanish.language import pages_url as spanish_pages_url
from ..types import PagesUrlsType

URLS: PagesUrlsType = english_pages_url

if os.environ['COURSE_LANGUAGE'] == 'spanish':
    URLS = spanish_pages_url


cs50x2024 = Blueprint(
    'cs50x2024',
    __name__,
    template_folder='templates'
)

cs50x2024.register_blueprint(weeks_bp, url_prefix=f"/{URLS['weeks']}")
cs50x2024.register_blueprint(notes_bp, url_prefix=f"/{URLS['notes']}")

from . import routes
