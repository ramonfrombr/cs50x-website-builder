import os
import google.generativeai as genai
from string import Template
import time

genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

prompt_template = Template(
    """Translate this text thoroughly from English to ${language}. Do not summarize. This is the text: ${text}""")

english_notes_dir = os.listdir("./app/cs50x2024/content/english/notes")
english_notes_dir.sort()

language = "spanish"


def translate_page_by_sections(files, page):

    destination_file = open(
        f"./app/cs50x2024/content/{language}/notes/{page}.md", "w")

    for file in files:
        source_text = open(
            f"./app/cs50x2024/content/english/notes/{file}").read()

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
                f"./app/cs50x2024/content/{language}/notes/{page}.md", "a")
            destination_file.write(response.text + "\n\n")
        except Exception as error:
            print("Error file: ", file)
            print("Error type: ", error)


for i in range(0, 10):
    sections = None
    if i == 1:
        sections = list(
            filter(lambda x: x.startswith(str(i)) and not x.startswith(str("10")), english_notes_dir))[1:]
    else:
        sections = list(
            filter(lambda x: x.startswith(str(i)), english_notes_dir))[1:]

    translate_page_by_sections(sections, str(i))
