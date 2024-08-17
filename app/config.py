import os
from .cs50x2024.content.english.language import menu as menu_english
from .cs50x2024.content.spanish.language import menu as menu_spanish
from .cs50x2024.content.french.language import menu as menu_french
from .cs50x2024.content.portuguese.language import menu as menu_portuguese
from .cs50x2024.content.english.language import pages_url as pages_url_english
from .cs50x2024.content.spanish.language import pages_url as pages_url_spanish
from .cs50x2024.content.french.language import pages_url as pages_url_french
from .cs50x2024.content.portuguese.language import pages_url as pages_url_portuguese


class Config(object):
    FREEZER_DESTINATION = "build_" + os.environ["COURSE_LANGUAGE"]


class EnglishConfig(Config):
    LANGUAGE = 'english',
    BACKGROUND_COLOR = '#a51c30'
    TITLE = "CS50x in English"
    INTRO = "CS50’s Introduction to Computer Science"
    DESCRIPTION = ""
    MENU_CS50X_2024 = menu_english
    PAGES_URLS = pages_url_english


class SpanishConfig(Config):
    LANGUAGE = 'spanish',
    BACKGROUND_COLOR = 'orangered'
    TITLE = "CS50x en Español"
    INTRO = "Curso de Introducción a la Ciencia de la Computación de la Universidad de Harvard"
    DESCRIPTION = ""
    MENU_CS50X_2024 = menu_spanish
    PAGES_URLS = pages_url_spanish


class FrenchConfig(Config):
    LANGUAGE = 'french',
    BACKGROUND_COLOR = 'darkblue'
    TITLE = "CS50x en Français"
    INTRO = ""
    DESCRIPTION = ""
    MENU_CS50X_2024 = menu_french
    PAGES_URLS = pages_url_french


class PortugueseConfig(Config):
    LANGUAGE = 'portuguese',
    BACKGROUND_COLOR = 'darkgreen'
    TITLE = "CS50x em Português"
    INTRO = ""
    DESCRIPTION = ""
    MENU_CS50X_2024 = menu_portuguese
    PAGES_URLS = pages_url_portuguese
