from flask import Flask
import os
from .config import EnglishConfig, SpanishConfig, FrenchConfig, PortugueseConfig


def create_app():
    app = Flask(__name__)

    if os.environ['COURSE_LANGUAGE'] == 'english':
        app.config.from_object(EnglishConfig)
    elif os.environ['COURSE_LANGUAGE'] == 'spanish':
        app.config.from_object(SpanishConfig)
    elif os.environ['COURSE_LANGUAGE'] == 'french':
        app.config.from_object(FrenchConfig)
    elif os.environ['COURSE_LANGUAGE'] == 'portuguese':
        app.config.from_object(PortugueseConfig)

    with app.app_context():
        from .cs50x2024 import cs50x2024
        app.register_blueprint(cs50x2024, url_prefix="/2024")
        from .core import core
        app.register_blueprint(core, url_prefix="/")
    return app
