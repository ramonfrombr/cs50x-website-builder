from .translate import translate
from get_files import get_files
from translate_types import TypeCourse, TypeLanguage
from constants import ContentTypes


def translate_psets(course: TypeCourse, language: TypeLanguage):
    files = get_files(course, ContentTypes.PSETS)
    translate(course, files, ContentTypes.PSETS, language, "html", "HTML file")
