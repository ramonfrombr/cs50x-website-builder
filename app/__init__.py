from flask import Flask
import os

from .cs50x.content.french.language import menu as menu_french
from .cs50x.content.portuguese.language import menu as menu_portuguese
from .cs50x.content.spanish.language import menu as menu_spanish
from .cs50x.content.english.language import menu as menu_english
from .cs50x.content.french.language import urls as urls_french
from .cs50x.content.portuguese.language import urls as urls_portuguese
from .cs50x.content.spanish.language import urls as urls_spanish
from .cs50x.content.english.language import urls as urls_english

from .python.content.french.language import menu as menu_french_python
from .python.content.portuguese.language import menu as menu_portuguese_python
from .python.content.spanish.language import menu as menu_spanish_python
from .python.content.english.language import menu as menu_english_python

def create_app():
    app = Flask(__name__)
    app.config["FREEZER_DESTINATION"] = "build_" + os.environ["COURSE_LANGUAGE"]

    if os.environ["COURSE_LANGUAGE"] == "portuguese":
        app.config["LANGUAGE"] = "portuguese"
        app.config["ASIDE_BG_COLOR"] = "green"
        app.config["LANGUAGE_MENU"] = menu_portuguese
        app.config["LANGUAGE_MENU_PYTHON"] = menu_portuguese_python
        app.config["URLS"] = urls_portuguese
        
    elif os.environ["COURSE_LANGUAGE"] == "spanish":
        app.config["LANGUAGE"] = "spanish"
        app.config["ASIDE_BG_COLOR"] = "red"
        app.config["LANGUAGE_MENU"] = menu_spanish
        app.config["LANGUAGE_MENU_PYTHON"] = menu_spanish_python
        app.config["URLS"] = urls_spanish

    elif os.environ["COURSE_LANGUAGE"] == "french":
        app.config["LANGUAGE"] = "french"
        app.config["ASIDE_BG_COLOR"] = "blue"
        app.config["LANGUAGE_MENU"] = menu_french
        app.config["LANGUAGE_MENU_PYTHON"] = menu_french_python
        app.config["URLS"] = urls_french

    elif os.environ["COURSE_LANGUAGE"] == "english":
        app.config["LANGUAGE"] = "english"
        app.config["ASIDE_BG_COLOR"] = "black"
        app.config["LANGUAGE_MENU"] = menu_english
        app.config["LANGUAGE_MENU_PYTHON"] = menu_english_python
        app.config["URLS"] = urls_english

    with app.app_context():
        from .cs50x import cs50x as cs50x_bp
        app.register_blueprint(cs50x_bp, url_prefix='/2024')
        from .tools import app as cs50_app
        app.register_blueprint(cs50_app, url_prefix='/')
 
        from .python import python as python_bp
        app.register_blueprint(python_bp, url_prefix='/python')
    return app