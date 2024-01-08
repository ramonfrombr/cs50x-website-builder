from .translate import translate
import os
from translate_types import TypeCourse
from constants import LABS_CHECKS
from get_files import get_files

def translate_labs_checks(course, language):
    checks = get_files(course, LABS_CHECKS)
    translate(course, checks, LABS_CHECKS, language, "py", "Python code")
