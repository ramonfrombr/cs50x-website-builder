from .translate import translate
from constants import LECTURES_CODE
from get_files import get_files

def translate_lectures_code(course, language):
    lectures_code = get_files(course, f"{LECTURES_CODE}/src5")
    lectures_code_html = list(filter(lambda file: file.endswith('html'), lectures_code))
    translate(course, lectures_code_html, f"{LECTURES_CODE}/src5", language, "html", "HTML language code")

    """
    source_code_folders = get_files(course, f"{LECTURES_CODE}")

    for srcFolder in source_code_folders:
        lectures_code = get_files(course, f"{LECTURES_CODE}/{srcFolder}")
        lectures_code_python = list(filter(lambda file: file.endswith('py'), lectures_code))
        lectures_code_html = list(filter(lambda file: file.endswith('html'), lectures_code))
 
        if lectures_code_python: 
            translate(course, lectures_code_python, f"{LECTURES_CODE}/{srcFolder}", language, "py", "Python language code")
        
        if lectures_code_html:
            translate(course, lectures_code_html, f"{LECTURES_CODE}/{srcFolder}", language, "html", "HTML language code")
    """