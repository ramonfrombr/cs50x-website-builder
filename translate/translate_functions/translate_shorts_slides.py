from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files
from constants import ContentTypes


def translate_shorts_slides(course: TypeCourse, language: TypeLanguage):
    slides = get_files(course, ContentTypes.SHORTS_SLIDES)
    translate(course, slides, ContentTypes.SHORTS_SLIDES, language, "txt", "text file")
