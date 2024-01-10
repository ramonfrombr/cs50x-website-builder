from .translate import translate
import os
from translate_types import TypeCourse
from ..constants import LECTURES_SCRIPTS
from get_files import get_files

def translate_lectures_scripts(course, language):

    numbers = ["2"]

    for number in numbers:

        lectures = get_files(course, f"{LECTURES_SCRIPTS}/{number}")

        translate(course, lectures[0:2], f"{LECTURES_SCRIPTS}/{number}", language, "txt", "text")
