from .translate import translate
from translate_types import TypeCourse,TypeLanguage
from get_files import get_files

def translate_psets_checks(course: TypeCourse, language: TypeLanguage):
    checks = get_files(course, "psets_checks")
    translate(course, checks, "psets_checks", language, "py", "Python code")
