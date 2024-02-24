from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files
from constants import ContentTypes

def translate_pages(course: TypeCourse, language: TypeLanguage):
    pages = list(filter(lambda file: file.endswith('.py'),get_files(course, "")))
    translate(course, pages, ContentTypes.PAGES, language, "py", "Python file")