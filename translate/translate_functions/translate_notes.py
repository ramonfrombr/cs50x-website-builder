from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files
from constants import ContentTypes

def translate_notes(course: TypeCourse, language: TypeLanguage):
    notes = get_files(course, ContentTypes.NOTES)
    translate(course, notes, ContentTypes.NOTES, language, "md", "Markdown file")