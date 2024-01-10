from .translate import translate
from files_names import manual
from constants import MANUAL

def translate_manual(course, language):
    translate(course, manual, MANUAL, language, "md", "Markdown file")
