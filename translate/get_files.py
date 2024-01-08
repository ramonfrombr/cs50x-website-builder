import os

def get_files(course, folder):
    """
    Returns a list of file names in specific course folder.
    """
    files = [file for file in os.listdir(os.getcwd() + f'/app/{course}/content/english/{folder}')]
    files.sort()
    return files