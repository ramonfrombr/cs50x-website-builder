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

from .python.content.english.language import menu_python as menu_python_english
from .python.content.spanish.language import menu_python as menu_python_spanish
from .python.content.french.language import menu_python as menu_python_french
from .python.content.portuguese.language import menu_python as menu_python_portuguese

from .ai.content.portuguese.language import menu_ai as menu_ai_portuguese


def create_app():
    app = Flask(__name__)
    app.config["FREEZER_DESTINATION"] = "build_" + os.environ["COURSE_LANGUAGE"]

    if os.environ["COURSE_LANGUAGE"] == "portuguese":
        app.config["LANGUAGE"] = "portuguese"
        app.config["ASIDE_BG_COLOR"] = "green"
        app.config["LANGUAGE_MENU"] = menu_portuguese
        app.config["LANGUAGE_MENU_PYTHON"] = menu_python_portuguese
        app.config["LANGUAGE_MENU_AI"] = menu_ai_portuguese
        app.config["URLS"] = urls_portuguese
        
    elif os.environ["COURSE_LANGUAGE"] == "spanish":
        app.config["LANGUAGE"] = "spanish"
        app.config["ASIDE_BG_COLOR"] = "red"
        app.config["LANGUAGE_MENU"] = menu_spanish
        app.config["LANGUAGE_MENU_PYTHON"] = menu_python_spanish
        app.config["URLS"] = urls_spanish

    elif os.environ["COURSE_LANGUAGE"] == "french":
        app.config["LANGUAGE"] = "french"
        app.config["ASIDE_BG_COLOR"] = "blue"
        app.config["LANGUAGE_MENU"] = menu_french
        app.config["LANGUAGE_MENU_PYTHON"] = menu_python_french
        app.config["URLS"] = urls_french

    elif os.environ["COURSE_LANGUAGE"] == "english":
        app.config["LANGUAGE"] = "english"
        app.config["ASIDE_BG_COLOR"] = "black"
        app.config["LANGUAGE_MENU"] = menu_english
        app.config["LANGUAGE_MENU_PYTHON"] = menu_python_english
        app.config["URLS"] = urls_english

    with app.app_context():
        from .cs50x import cs50x as cs50x_bp
        app.register_blueprint(cs50x_bp, url_prefix='/2023')
        from .tools import app as cs50_app
        app.register_blueprint(cs50_app, url_prefix='/') 
        from .python import python as python_bp
        app.register_blueprint(python_bp, url_prefix='/python')
        from .web import web as web_bp
        app.register_blueprint(web_bp, url_prefix='/web')
        from .ai import ai as ai_bp
        app.register_blueprint(ai_bp, url_prefix='/ai')
 
    return app
