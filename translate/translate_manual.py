import os
import google.generativeai as genai
from string import Template

genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

prompt_template = Template(
    """Translate this text thoroughly from English to ${language}. Do not summarize. This is the text: ${text}""")

english_content_dir = os.listdir(
    "./app/core/templates/core/languages/english/manual")
english_content_dir.sort()

english_content_dir = list(filter(lambda x: not x.startswith(
    'blank') and not x.startswith('layout'), english_content_dir))

print(english_content_dir)

language = "french"


def translate_manual_html(pages):
    for file in pages:
        source_text = open(
            f"./app/core/templates/core/languages/english/manual/{file}").read()

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
                f"./app/core/templates/core/languages/{language}/manual/{file}", "w")
            destination_file.write(response.text)
        except:
            print("Error: ", file)


translate_manual_html(english_content_dir)
