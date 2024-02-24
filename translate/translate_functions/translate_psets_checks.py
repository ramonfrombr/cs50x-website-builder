from .translate import translate
from translate_types import TypeCourse,TypeLanguage
from get_files import get_files
from constants import ContentTypes


def translate_psets_checks(course: TypeCourse, language: TypeLanguage):
    checks = get_files(course, ContentTypes.PSETS_CHECKS)
    translate(course, checks, ContentTypes.PSETS_CHECKS, language, "py", "Python code")
