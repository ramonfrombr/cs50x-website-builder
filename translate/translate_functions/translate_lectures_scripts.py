from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from constants import ContentTypes
from get_files import get_files

def translate_lectures_scripts(course: TypeCourse, language: TypeLanguage):
    numbers = range(0,10)
    for number in numbers:
        lectures = get_files(course, f"{ContentTypes.LECTURES_SCRIPTS}/{number}")
        translate(course, lectures, f"{ContentTypes.LECTURES_SCRIPTS}/{number}", language, "txt", "text")
