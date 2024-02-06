from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files

def translate_pages(course: TypeCourse, language: TypeLanguage):
    pages = list(filter(lambda file: file.endswith('.md'),get_files(course, "")))
    translate(course, pages, "pages", language, "md", "Markdown file")