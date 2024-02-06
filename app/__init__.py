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

# import menus
from .web.content.english.language import menu as menu_english_web
from .web.content.french.language import menu as menu_french_web
from .web.content.spanish.language import menu as menu_spanish_web
from .web.content.portuguese.language import menu as menu_portuguese_web
from .web.content.japanese.language import menu as menu_japanese_web
from .web.content.chinese.language import menu as menu_chinese_web
from .web.content.german.language import menu as menu_german_web
from .web.content.italian.language import menu as menu_italian_web
from .web.content.korean.language import menu as menu_korean_web
from .python.content.french.language import menu as menu_french_python
from .python.content.portuguese.language import menu as menu_portuguese_python
from .python.content.spanish.language import menu as menu_spanish_python
from .python.content.english.language import menu as menu_english_python

def create_app():
    app = Flask(__name__)
    app.config["FREEZER_DESTINATION"] = "build_" + os.environ["COURSE_LANGUAGE"]

    if os.environ["COURSE_LANGUAGE"] == "portuguese":
        # portuguese config
        app.config["LANGUAGE_MENU_web"] = menu_portuguese_web
        app.config["LANGUAGE_MENU_python"] = menu_portuguese_python
        app.config["LANGUAGE_MENU"] = menu_portuguese
        app.config["LANGUAGE"] = "portuguese"
        app.config["ASIDE_BG_COLOR"] = "green"
        app.config["URLS"] = urls_portuguese
    elif os.environ["COURSE_LANGUAGE"] == "spanish":
        # spanish config
        app.config["LANGUAGE_MENU_web"] = menu_spanish_web
        app.config["LANGUAGE_MENU_python"] = menu_spanish_python
        app.config["LANGUAGE_MENU"] = menu_spanish
        app.config["LANGUAGE"] = "spanish"
        app.config["ASIDE_BG_COLOR"] = "red"
        app.config["URLS"] = urls_spanish
    elif os.environ["COURSE_LANGUAGE"] == "french":
        # french config
        app.config["LANGUAGE_MENU_web"] = menu_french_web
        app.config["LANGUAGE_MENU_python"] = menu_french_python
        app.config["LANGUAGE_MENU"] = menu_french
        app.config["LANGUAGE"] = "french"
        app.config["ASIDE_BG_COLOR"] = "blue"
        app.config["URLS"] = urls_french
    elif os.environ["COURSE_LANGUAGE"] == "english":
        # english config
        app.config["LANGUAGE_MENU_web"] = menu_english_web
        app.config["LANGUAGE_MENU_python"] = menu_english_python
        app.config["LANGUAGE_MENU"] = menu_english
        app.config["LANGUAGE"] = "english"
        app.config["ASIDE_BG_COLOR"] = "black"
        app.config["URLS"] = urls_english

    with app.app_context():
        # Blueprint register (this line is used by the cour_folder_builder. don't remove)

        from .web import web as web_bp
        app.register_blueprint(web_bp, url_prefix='/web')
        from .cs50x import cs50x as cs50x_bp
        app.register_blueprint(cs50x_bp, url_prefix='/2024')
        from .tools import app as cs50_app
        app.register_blueprint(cs50_app, url_prefix='/')
        from .python import python as python_bp
        app.register_blueprint(python_bp, url_prefix='/python')
    return app