import os
import google.generativeai as genai
from string import Template
import time

language = "spanish"

genai.configure(api_key="AIzaSyBuWjvX5pyR6I7p_SxgwrD4nVx00ZpD-ZI")
model = genai.GenerativeModel('gemini-1.0-pro-latest')

prompt_template = Template(
    """Translate this code from English to ${language}: ${text}""")

source_code_dirs = os.listdir(
    "./app/cs50x2024/content/english/lectures_source_code")

source_code_dirs.sort()


def translate_src1_to_src5():
    for directory in source_code_dirs[1:6]:

        source_code_files = os.listdir(
            f"./app/cs50x2024/content/english/lectures_source_code/{directory}")

        source_code_files = list(
            filter(lambda x: ".py" in x or ".c" in x, source_code_files))

        source_code_files.sort()

        for file in source_code_files:
            source_text = open(
                f"./app/cs50x2024/content/english/lectures_source_code/{directory}/{file}").read()

            prompt = prompt_template.substitute(
                text=source_text, language=language)

            try:
                response = model.generate_content(prompt)
                destination_file = open(
                    f"./app/cs50x2024/content/{language}/lectures_source_code/{directory}/{file}", "w")
                destination_file.write(response.text)
            except Exception as error:
                print("Error file: ", file)
                print("Error type: ", error)

            time.sleep(5)


def translate_src6():
    src6_dirs = os.listdir(
        "./app/cs50x2024/content/english/lectures_source_code/src6")
    src6_dirs.sort()

    for directory in src6_dirs:
        src6_files = os.listdir(
            f"./app/cs50x2024/content/english/lectures_source_code/src6/{directory}")

        for file in src6_files:
            source_text = open(
                f"./app/cs50x2024/content/english/lectures_source_code/src6/{directory}/{file}").read()

            prompt = prompt_template.substitute(
                text=source_text, language=language)

            try:
                response = model.generate_content(prompt)
                destination_file = open(
                    f"./app/cs50x2024/content/{language}/lectures_source_code/src6/{directory}/{file}", "w")
                destination_file.write(response.text)
            except Exception as error:
                print("Error file: ", file)
                print("Error type: ", error)

            time.sleep(5)

        print(src6_files)


translate_src1_to_src5()
translate_src6()
