import os
import sys
from termcolor import colored

def check(COURSE, LANGUAGE):
    english_files_list = os.listdir(f'app/{COURSE}/content/english')
    english_files_list.sort()

    language_files_list = os.listdir(f'app/{COURSE}/content/{LANGUAGE}')
    language_files_list.sort()

    english_files_set = set(english_files_list)
    language_files_set = set(language_files_list)
    files_not_created = english_files_set.difference(language_files_set)

    folders_not_created = get_folder_names_from_filenames(files_not_created)

    if len(folders_not_created)>0: create_folders(COURSE, LANGUAGE, folders_not_created)

    print("######################")
    for folder in get_folder_names_from_filenames(english_files_list):
        check_inside_content_folders(COURSE, LANGUAGE, folder)
        print("\n######################\n")



def check_inside_content_folders(course, language, folder):
    print(f'FOLDER: {folder}')

    files_not_created = get_files_not_created(course, language, folder)

    if len(files_not_created):
        print(f'\n{len(files_not_created)} files not created:')
        print(files_not_created)
    else:
        print(colored('\nAll files created :)', 'green'))


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
