import os
import google.generativeai as genai
from string import Template

genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

prompt_template = Template(
    """Translate this text thoroughly from English to ${language}. Do not summarize. This is the text: ${text}""")

english_content_dir = os.listdir("./app/cs50x2024/content/english")
pages_files = list(filter(lambda f: ".md" in f, english_content_dir))
pages_files.sort()

language = "spanish"

single_pages = list(
    filter(lambda f: 'project' not in f and 'style' not in f and 'faqs' not in f, pages_files))


def translate_single_pages(pages):
    for file in pages:
        source_text = open(f"./app/cs50x2024/content/english/{file}").read()

        prompt = prompt_template.substitute(
            text=source_text, language=language)

        try:
            response = model.generate_content(prompt)
            destination_file = open(
                f"./app/cs50x2024/content/{language}/{file}", "w")
            destination_file.write(response.text)
        except:
            print("Error: ", file)


def translate_page_by_sections(files, page):

    destination_file = open(
        f"./app/cs50x2024/content/{language}/{page}.md", "w")

    for file in files:
        source_text = open(f"./app/cs50x2024/content/english/{file}").read()

        prompt = prompt_template.substitute(
            text=source_text, language=language)

        try:
            response = model.generate_content(prompt)
            destination_file = open(
                f"./app/cs50x2024/content/{language}/{page}.md", "a")
            destination_file.write(response.text + "\n\n")
        except:
            print("Error: ", file)


final_project_files = list(filter(lambda f: 'project' in f, pages_files))
final_project_files_sections = final_project_files[1:]

style_guide_files = list(filter(lambda f: 'style' in f, pages_files))
style_guide_files_sections = style_guide_files[1:]

faqs_files = list(filter(lambda f: 'faqs' in f, pages_files))
faqs_files_sections = faqs_files[1:]

# translate_page_by_sections(final_project_files_sections, "project")
# translate_page_by_sections(style_guide_files_sections, "style")
translate_page_by_sections(faqs_files_sections, "faqs")
# translate_single_pages(single_pages)
