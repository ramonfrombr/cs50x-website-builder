import os
from translate_types import TypeCourse, TypeLanguage, TypeContent
from format import replace_incorrect_translations, replace_incorrect_translations_checks, remove_leading_and_trailing_quote

def generate_system_message(extension: str, language: TypeLanguage):

    SYSTEM_MESSAGE_PYTHON = f"You are a helpful assistant that translates Python language code from English to {language.capitalize()}. Translate the function names also."

    SYSTEM_MESSAGE_C = f"You are a helpful assistant that translates C language code from English to {language.capitalize()}. Translate the function names also."

    SYSTEM_MESSAGE_MARKDOWN = f"You are a helpful assistant that translates computer science related content from English to {language.capitalize()}. Translate the text thoroughly. Do not summarize the translation. Do not convert HTML tags to Markdown."

    if (extension=="py"):
        return SYSTEM_MESSAGE_PYTHON
    elif (extension=="c"):
        return SYSTEM_MESSAGE_C
    else:
        return SYSTEM_MESSAGE_MARKDOWN

def generate_prompt(file_description: str, language: TypeLanguage, source_file):
    return f'Translate the following computer science {file_description} from English to {language.capitalize()}: {source_file}'

def generate_file_psets(
        course: TypeCourse,
        folder: TypeContent,
        filename: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
    
    current_directory = os.getcwd()

    file_destination = f"{current_directory}/app/{course}/content/{language}/{folder}"

    # Creates folder if not exists
    if not (os.path.exists(file_destination)):
        os.makedirs(file_destination)

    new_file = open(f'{file_destination}/{filename}', 'w')
    new_file.writelines(translated_content)

def generate_file_manual(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
        
    current_directory = os.getcwd()

    file_destination = f"{current_directory}/app/tools/content/{language}/{folder}"

    # Creates folder if not exists
    if not (os.path.exists(file_destination)):
        os.makedirs(file_destination)

    translated_content = remove_leading_and_trailing_quote(translated_content)

    new_file = open(f'{file_destination}/{f}.{extension}', 'w')
    new_file.writelines(translated_content)

def generate_file_psets_code(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
    
    current_directory = os.getcwd()
    
    file_destination = f"{current_directory}/app/{course}/content/{language}/{folder}/{f}"

    # Creates folder if not exists
    if not (os.path.exists(file_destination)):
        os.makedirs(file_destination)

    new_file = open(f'{file_destination}/{f}.{extension}', 'w')
    translated_content = replace_incorrect_translations(translated_content)
    translated_content = remove_leading_and_trailing_quote(translated_content)
    new_file.writelines(translated_content)

def generate_file_psets_checks(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):

    current_directory = os.getcwd()

    file_destination = f"{current_directory}/app/{course}/content/{language}/{folder}/{f}"
        
    # Creates folder if not exists
    if not (os.path.exists(file_destination)):
        os.makedirs(file_destination)

    generated_file = open(f'app/{course}/content/{language}/{folder}/{f}/__init__.{extension}', 'w')

    generated_file.writelines(replace_incorrect_translations_checks(translated_content))

    source_cs50yml = open(f"app/{course}/content/english/{folder}/{f}/.cs50.yml", "r")
    cs50yml = open(f'app/{course}/content/{language}/{folder}/{f}/.cs50.yml', 'w')
    cs50yml.writelines(source_cs50yml.readlines())

def generate_file_notes(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
    current_directory = os.getcwd()
    file_destination = f"{current_directory}/app/{course}/content/{language}/{folder}"
    
    # Creates folder if not exists
    if not (os.path.exists(file_destination)):
        os.makedirs(file_destination)

    generated_file = open(f'{file_destination}/{f}', 'a')
    generated_file.writelines("\n\n"+translated_content)

def generate_file_specifications(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
    current_directory = os.getcwd()
    file_destination = f"{current_directory}/app/{course}/content/{language}/{folder}"
    
    # Creates folder if not exists
    if not (os.path.exists(file_destination)):
        os.makedirs(file_destination)

    generated_file = open(f'{file_destination}/{f}', 'a')
    generated_file.writelines("\n\n"+translated_content)


def generate_file(
        course: TypeCourse,
        folder: TypeContent,
        f: str,
        language: TypeLanguage,
        extension: str,
        translated_content: str):
    
    file_destination = f'app/{course}/content/{language}/{folder}/{f}'
    generated_file = open(file_destination, 'w')
    generated_file.writelines(translated_content)
