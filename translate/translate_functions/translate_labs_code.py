from .translate import translate
from constants import LABS_CODE

def translate_labs_code(course, language):
    code = ["inheritance", "scrabble", "volume"]
    translate(course, code, LABS_CODE, language, "c", "C code")
   