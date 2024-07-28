from .cs50x2024.content.english.language import menu as menu_english
from .cs50x2024.content.spanish.language import menu as menu_spanish


class Config(object):
    pass


class EnglishConfig(Config):
    LANGUAGE = 'english',
    BACKGROUND_COLOR = '#a51c30'
    TITLE = "CS50x in English"
    INTRO = "CS50’s Introduction to Computer Science"
    MENU_CS50X_2024 = menu_english


class SpanishConfig(Config):
    LANGUAGE = 'spanish',
    BACKGROUND_COLOR = 'orangered'
    TITLE = "CS50x en Español"
    INTRO = "Curso de Introducción a la Ciencia de la Computación de la Universidad de Harvard"
    MENU_CS50X_2024 = menu_spanish
