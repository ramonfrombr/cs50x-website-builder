import os
import google.generativeai as genai
from string import Template

genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

prompt_template = Template(
    """Translate this text thoroughly from English to ${language}. Do not summarize. This is the text: ${text}""")

english_content_dir = os.listdir(
    "./app/cs50x2024/content/english/shorts_slides_text")

english_content_dir.sort()

language = "spanish"


def translate_pages(pages):
    for file in pages:
        source_text = open(
            f"./app/cs50x2024/content/english/shorts_slides_text/{file}").read()

        prompt = prompt_template.substitute(
            text=source_text, language=language)

        try:
            response = model.generate_content(prompt)
            destination_file = open(
                f"./app/cs50x2024/content/{language}/shorts_slides_text/{file}", "w")
            destination_file.write(response.text)
        except:
            print("Error: ", file)


translate_pages(english_content_dir)
