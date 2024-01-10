from .translate import translate
from get_files import get_files

def translate_psets(course, language):
    files = get_files(course, "psets")
    translate(course, files, "psets", language, "html", "HTML file")
