import openai
import time
from dotenv import load_dotenv
load_dotenv()  
import os
from generate import generate_file, generate_prompt, generate_system_message, generate_prompt_notes, generate_file_manual, generate_file_notes, generate_file_psets, generate_file_psets_checks, generate_file_psets_code
from translate_types import TypeCourse, TypeLanguage, TypeContent
from typing import List

openai.api_key = os.getenv('CHATGPT_KEY')

def get_chatgpt_translation(system_message: str, prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
    )
    translation = response.choices[0].message.content
    return translation

def get_translation_and_generate_file(system_message, prompt, course, folder, filename, language, extension):

    try:
        translation = get_chatgpt_translation(system_message, prompt)

        if folder=="psets":
            generate_file_psets(course, folder, filename, language, extension, translation)
        elif folder=="psets_code" or folder=="labs_code":
            generate_file_psets_code(course, folder, filename, language, extension, translation)
        elif folder=="psets_checks" or folder=="psets_checks":
            generate_file_psets_checks(course, folder, filename, language, extension, translation)
        elif folder=="notes":
            generate_file_notes(course, folder, filename, language, extension, translation)
        elif folder=="manual":
            generate_file_manual(course, folder, filename, language, extension, translation)
        else:
            generate_file(course, folder, filename, language, extension, translation)

    except openai.error.InvalidRequestError:
        print(f">>>> Error: there was an error when translating '{filename}'")
    time.sleep(20)

def translate(
        course: TypeCourse,
        files: List[str],
        folder: TypeContent,
        language: TypeLanguage,
        extension: str,
        file_description: str):
    
    FOLDER_NOTES = "notes"
    FOLDER_LABS_CODE = "labs_code"
    FOLDER_PSETS_CODE = "psets_code"
    FOLDER_LABS_CHECKS = "labs_checks"
    FOLDER_PSETS_CHECKS = "psets_checks"

    # Defines root folder
    if folder=="manual":
        root_folder = "app/tools/content/english"
    else:
        root_folder = f"app/{course}/content/english"

    system_message = generate_system_message(extension, language)
    
    for filename in files:
        try:

            if (folder==FOLDER_NOTES):

                source_file = open(f"{root_folder}/{folder}/{filename}", "r")

                notes_chunks = source_file.read().split("\n## ")

                for chunk in notes_chunks:
                    prompt = generate_prompt_notes(file_description, language, "\n## "+chunk)
                    get_translation_and_generate_file(system_message, prompt, course, folder, filename, language, extension)

            else:
                if (folder==FOLDER_LABS_CODE or folder==FOLDER_PSETS_CODE):
                    source_file = open(f"{root_folder}/{folder}/{filename}/{filename}.{extension}", "r")
                elif (folder==FOLDER_LABS_CHECKS or folder==FOLDER_PSETS_CHECKS):
                    source_file = open(f"{root_folder}/{folder}/{filename}/__init__.{extension}", "r")
                else:
                    source_file = open(f"{root_folder}/{folder}/{filename}.{extension}", "r")

                prompt = generate_prompt(file_description, language, source_file)
                get_translation_and_generate_file(system_message, prompt, course, folder, filename, language, extension)

        except:
            print(f">>> Error: couldn't open the file '{filename}'")
            pass
