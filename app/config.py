class Config(object):
    pass


class EnglishConfig(Config):
    LANGUAGE = 'english',
    BACKGROUND_COLOR = '#a51c30'
    TITLE = "CS50x in English"
    INTRO = "CS50’s Introduction to Computer Science"


class SpanishConfig(Config):
    LANGUAGE = 'spanish',
    BACKGROUND_COLOR = 'orangered'
    TITLE = "CS50x en Español"
    INTRO = "Curso de Introducción a la Ciencia de la Computación de la Universidad de Harvard"
