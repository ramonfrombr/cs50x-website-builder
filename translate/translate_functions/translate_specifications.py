from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files
from constants import ContentTypes

def translate_specifications(course: TypeCourse, language: TypeLanguage):
    specifications = get_files(course, ContentTypes.SPECIFICATIONS)
    translate(course, specifications, ContentTypes.SPECIFICATIONS, language, "md", "Markdown file")