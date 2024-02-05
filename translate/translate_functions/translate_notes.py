from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files

def translate_notes(course: TypeCourse, language: TypeLanguage):
    notes = get_files(course, "notes")
    translate(course, notes, "notes", language, "md", "Markdown file")