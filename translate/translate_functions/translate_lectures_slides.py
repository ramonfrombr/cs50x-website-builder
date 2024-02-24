from .translate import translate
from translate_types import TypeCourse, TypeLanguage
from constants import ContentTypes
from get_files import get_files
import os
import fitz # imports the pymupdf library

def convert_pdf_to_text(course, content_type):
    slides = get_files(course, f"{content_type}_pdf")
    
    for slide in slides:
        doc = fitz.open(os.getcwd() + f'/app/{course}/content/english/{content_type}_pdf/{slide}') # open a document
        pdf_text = ""
        for idx, page in enumerate(doc): # iterate the document pages
            text = page.get_text() # get plain text encoded as UTF-8
            pdf_text = pdf_text + f"\nSlide [{idx}]\n\n" + text
    
        new_file = open(os.getcwd() + f"/app/{course}/content/english/{content_type}_text/{slide.split('.')[0]}.txt", "w")
        new_file.write(pdf_text)
        new_file.close()

def translate_lectures_slides(course: TypeCourse, language: TypeLanguage):
    # Convert pdf to text
    convert_pdf_to_text(course, ContentTypes.LECTURES_SLIDES)
    slides = get_files(course, f"{ContentTypes.LECTURES_SLIDES}_text")
    translate(course, slides, f"{ContentTypes.LECTURES_SLIDES}", language, "txt", "text")
