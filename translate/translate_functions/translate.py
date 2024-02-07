import time
from dotenv import load_dotenv
load_dotenv()  
import os
from generate import generate_prompt, generate_system_message, generate_file_manual, generate_file_notes, generate_file_psets, generate_file_psets_checks, generate_file_psets_code, generate_file_specifications, generate_file_pages
from translate_types import TypeCourse, TypeLanguage, TypeContent
from typing import List
from openai import OpenAI
from constants import ContentTypes

client = OpenAI(api_key=os.getenv('CHATGPT_KEY'))

def get_chatgpt_translation(system_message: str, prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    translation = response.choices[0].message.content
    return translation

def generate_file(translation, course, folder, filename, language, extension):
    try:
        if ContentTypes.LECTURES_CODE in folder:
            generate_file_psets(course, folder, filename, language, extension, translation)
        else:
            match folder:
                case ContentTypes.PSETS:
                    generate_file_psets(course, folder, filename, language, extension, translation)
                case ContentTypes.PSETS_CODE | ContentTypes.LABS_CODE:
                    generate_file_psets_code(course, folder, filename, language, extension, translation)
                case ContentTypes.PSETS_CHECKS | ContentTypes.LABS_CHECKS:
                    generate_file_psets_checks(course, folder, filename, language, extension, translation)
                case ContentTypes.NOTES:
                    generate_file_notes(course, folder, filename, language, extension, translation)
                case ContentTypes.SPECIFICATIONS:
                    generate_file_specifications(course, folder, filename, language, extension, translation)
                case ContentTypes.MANUAL:
                    generate_file_manual(course, folder, filename, language, extension, translation)
                case _:
                    generate_file_pages(course, folder, filename, language, extension, translation)
    except Exception as e:
        print(f"Error: there was an error when generating file '{filename}'")
        print(e)
    
def define_root_folder(folder, course):
  if folder=="manual":
    return "app/tools/content/english"
  return f"app/{course}/content/english"

def translate(
        course: TypeCourse,
        files: List[str],
        folder: TypeContent,
        language: TypeLanguage,
        extension: str,
        file_description: str):

    root_folder = define_root_folder(folder, course)
    system_message = generate_system_message(extension, language)

    for filename in files:
        try:
            if (folder==ContentTypes.NOTES):
                source_file = open(f"{root_folder}/{folder}/{filename}", "r")
                file_chunks = source_file.read().split("\n## ")

                for idx, chunk in enumerate(file_chunks):
                    if idx == 0:
                      prompt = generate_prompt(file_description, language, chunk)
                    else:
                      prompt = generate_prompt(file_description, language, "\n## "+chunk)
                    translation = get_chatgpt_translation(system_message, prompt)
                    generate_file(translation, course, folder, filename, language, extension)
            elif (folder==ContentTypes.SPECIFICATIONS):
                source_file = open(f"{root_folder}/{folder}/{filename}", "r").read()
                prompt = generate_prompt(file_description, language, source_file)
                translation = get_chatgpt_translation(system_message, prompt)
                generate_file(translation, course, folder, filename, language, extension)
            elif ContentTypes.LECTURES_CODE in folder:
                source_file = open(f"{root_folder}/{folder}/{filename}", "r").read()
                prompt = generate_prompt(file_description, language, source_file)
                translation = get_chatgpt_translation(system_message, prompt)
                generate_file(translation, course, folder, filename, language, extension)
            else:
                if (folder==ContentTypes.LABS_CODE or folder==ContentTypes.PSETS_CODE):
                    source_file = open(f"{root_folder}/{folder}/{filename}/{filename}.{extension}", "r").read()
                elif (folder==ContentTypes.LABS_CHECKS or folder==ContentTypes.PSETS_CHECKS):
                    filepath = f"{root_folder}/{folder}/{filename}/__init__.{extension}"
                    source_file = open(filepath, "r").read()
                elif (folder==ContentTypes.PAGES):
                    source_file = open(f"{root_folder}/{filename}", "r").read()
                else:
                    source_file = open(f"{root_folder}/{folder}/{filename}", "r").read()
                
                prompt = generate_prompt(file_description, language, source_file)
                translation = get_chatgpt_translation(system_message, prompt)
                generate_file(translation, course, folder, filename, language, extension)
                
        except Exception as e:
            print(f"Error: couldn't open the file '{filename}'")
            print(e)
                    
        time.sleep(21)
