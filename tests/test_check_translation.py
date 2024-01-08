import os
from translate.check_translation import get_folder_names_from_filenames, create_folders

def test_get_folder_names_from_filenames():
    files = ["a", "b", "a.md", "a.py"]
    assert get_folder_names_from_filenames(files) == ["a", "b"]

def test_create_folders():
    COURSE = "cs50x"
    LANGUAGE = "portuguese"

    folders_to_create = ["test_folder_1", "test_folder_2", "test_folder_3"]

    create_folders(COURSE, LANGUAGE, folders_to_create)

    all_folders = os.listdir(f'app/{COURSE}/content/{LANGUAGE}')
    
    assert all(i in all_folders for i in folders_to_create)

    for folder in folders_to_create:
        os.rmdir(f'app/{COURSE}/content/{LANGUAGE}/{folder}')
    