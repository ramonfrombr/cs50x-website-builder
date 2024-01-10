from .translate import translate
import os
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files
from constants import SHORTS_SLIDES

def translate_shorts_slides(course: TypeCourse, language: TypeLanguage):
    slides = get_files(course, SHORTS_SLIDES)
    translate(course, slides, SHORTS_SLIDES, language, "txt", "text file")
