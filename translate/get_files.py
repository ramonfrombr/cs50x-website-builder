import os

def get_files(course, folder):
    return [file for file in os.listdir(os.getcwd() + f'app/{course}/content/english/{folder}')]
