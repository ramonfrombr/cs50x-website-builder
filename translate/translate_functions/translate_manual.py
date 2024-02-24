from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from get_files import get_files
from constants import ContentTypes
import os

def translate_manual(course: TypeCourse, language: TypeLanguage):
    #markdown_files = get_files("tools", ContentTypes.MANUAL)
    #translate(course, markdown_files, ContentTypes.MANUAL, language, "md", "Markdown file")
    html_files = [file for file in os.listdir(os.getcwd() + f'/app/templates/english/manual')]
    print(html_files)