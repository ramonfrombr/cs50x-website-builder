from .translate import translate
from constants import LECTURES_CODE
from get_files import get_files

def translate_lectures_code(course, language):
    n_source_code_folders = len(get_files(course, f"{LECTURES_CODE}"))

    for i in range(6,n_source_code_folders):
      
      lectures_code = get_files(course, f"{LECTURES_CODE}/src{i}")

      lectures_code = list(filter(lambda file: file.endswith('py'), lectures_code))

      translate(course, lectures_code, f"{LECTURES_CODE}/src{i}", language, "py", "Python language code")