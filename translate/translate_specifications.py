import os
import google.generativeai as genai
from string import Template

genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

prompt_template = Template(
    """Translate this text thoroughly from English to ${language}. Do not summarize. This is the text: ${text}""")

english_specifications_dir = os.listdir(
    "./app/cs50x2024/content/english/specifications")
english_specifications_dir.sort()

language = "spanish"


def translate_specifications_pages(pages):
    for file in pages:
        source_text = open(
            f"./app/cs50x2024/content/english/specifications/{file}").read()

        prompt = prompt_template.substitute(
            text=source_text, language=language)

        try:
            response = model.generate_content(prompt, safety_settings=[
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            ])
            destination_file = open(
                f"./app/cs50x2024/content/{language}/specifications/{file}", "w")
            destination_file.write(response.text)
        except:
            print("Error: ", file)


specifications_sections = ["birthdays", "caesar", "cash", "dna", "filter_less", "filter_more", "finance", "inheritance", "mario_less", "movies",
                           "plurality", "readability", "recover", "runoff", "scrabble", "songs", "speller", "tideman", "trivia", "volume"]

specifications_without_sections = list(filter(lambda x: not x.startswith(
    tuple(specifications_sections)), english_specifications_dir))

translate_specifications_pages(specifications_without_sections)

specifications_with_sections = list(filter(lambda x: x.startswith(
    tuple(specifications_sections)), english_specifications_dir))

groups = []
for specification in specifications_sections:
    sublist = list(filter(lambda x: x.startswith(
        specification), specifications_with_sections))
    sublist.sort()
    groups.append(sublist)


def translate_specification_by_sections(files, page):

    destination_file = open(
        f"./app/cs50x2024/content/{language}/specifications/{page}", "w")

    for file in files:
        source_text = open(
            f"./app/cs50x2024/content/english/specifications/{file}").read()

        prompt = prompt_template.substitute(
            text=source_text, language=language)

        try:
            response = model.generate_content(prompt, safety_settings=[
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            ])
            destination_file = open(
                f"./app/cs50x2024/content/{language}/specifications/{page}", "a")
            destination_file.write(response.text + "\n\n")
        except Exception as error:
            print("Error file: ", file)
            print("Error type: ", error)


for group in groups:
    translate_specification_by_sections(group[1:], group[0])


# translate_specification_by_sections(groups[0][1:], groups[0][0])
