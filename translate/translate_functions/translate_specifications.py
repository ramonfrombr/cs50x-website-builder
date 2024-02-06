from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files

def translate_specifications(course: TypeCourse, language: TypeLanguage):
    specifications = get_files(course, "specifications")
    translate(course, specifications, "specifications", language, "md", "Markdown file")