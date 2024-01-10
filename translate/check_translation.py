import os
import sys
from termcolor import colored
import math

def check(COURSE, LANGUAGE):
    print("Checking translation progress...\n")

    # Determines which files weren't created
    english_files_list = get_files_and_folders_in_course(COURSE, "english")
    english_files_list.sort()
    language_files_list = get_files_and_folders_in_course(COURSE, LANGUAGE)
    language_files_list.sort()
    english_files_set = set(english_files_list)
    language_files_set = set(language_files_list)
    files_not_created = english_files_set.difference(language_files_set)

    folders_not_created = get_folder_names_from_filenames(files_not_created)
    if len(folders_not_created)>0:
        create_folders(COURSE, LANGUAGE, folders_not_created)

    for folder in get_folder_names_from_filenames(english_files_list):
        check_translation_progress_in_folder(COURSE, LANGUAGE, folder)

def check_translation_progress_in_folder(course, language, folder):
    print(f'Folder: {folder}')
    files_not_created = get_files_not_created(course, language, folder)
    n_files_english = len(get_files_in_folder(course, folder, "english"))
    n_files_language = len(get_files_in_folder(course, folder, language))
    print(f"Files to translate: {n_files_english}")
    print(f"Files translated: {n_files_language}")
    # Calculates progress percentage
    percentage_translated = n_files_language/n_files_english*100
    n_bars_progress_completed = math.floor(percentage_translated/5)
    n_bars_progress_remaining = 20 - n_bars_progress_completed
    progress_bar = "▮"*n_bars_progress_completed
    remaining_progress_bar = "▯"*n_bars_progress_remaining
    print(f"Progress: {percentage_translated:3.0f}% [{progress_bar}{remaining_progress_bar}]")
    # Report message
    if n_files_language==0:
        print(colored(f'No files were translated.', 'red'))
    elif len(files_not_created):
        print(colored(f'There are {len(files_not_created)} files left to translate.', 'yellow'))
    else:
        print(colored('All files translated :)', 'green'))
    print()

def get_files_and_folders_in_course(course, language):
    return os.listdir(f'app/{course}/content/{language}')

def get_files_in_folder(course, folder, language):
    return os.listdir(f'app/{course}/content/{language}/{folder}')

def get_files_not_created(course, language, folder):
    english_files = os.listdir(f'app/{course}/content/english/{folder}')
    language_files = os.listdir(f'app/{course}/content/{language}/{folder}')
    english_files.sort()
    language_files.sort()
    english_files_set = set(english_files)
    language_files_set = set(language_files)
    files_not_created_set = english_files_set.difference(language_files_set)
    files_not_created_list = list(files_not_created_set)
    files_not_created_list.sort()
    return files_not_created_list

def get_folder_names_from_filenames(files):
    except_markdown = [file for file in files if '.md' not in file]
    except_markdown_and_python = [file for file in except_markdown if '.py' not in file]
    except_markdown_and_python_and_pycache = [file for file in except_markdown_and_python if '__pycache__' not in file]

    return except_markdown_and_python_and_pycache

def create_folders(course, language, folders):
    for folder in folders:
        os.makedirs(f"app/{course}/content/{language}/{folder}")
