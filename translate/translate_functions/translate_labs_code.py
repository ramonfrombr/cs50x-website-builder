from translate_types import TypeCourse, TypeLanguage
from .translate import translate
from constants import ContentTypes

def translate_labs_code(course: TypeCourse, language: TypeLanguage):
    code = ["inheritance", "scrabble", "volume"]
    translate(course, code, ContentTypes.LABS_CODE, language, "c", "C code")
   