from flask import render_template
from . import python as bp
import os
import marko

honesty_urls = {
  "english": "honesty",
  "portuguese": "honestidade",
  "french": "honnetete",
  "spanish": "honestidad"
}

faqs_urls = {
  "english": "faqs",
  "portuguese": "perguntas_frequentes",
  "french": "faqs",
  "spanish": "faqs"
}

certificate_urls = {
  "english": "certificate",
  "portuguese": "certificado",
  "french": "certificat",
  "spanish": "certificado"
}

syllabus_urls = {
  "english": "syllabus",
  "portuguese": "curriculum",
  "french": "programme",
  "spanish": "programa"
}

staff_urls = {
  "english": "staff",
  "portuguese": "equipe",
  "french": "equipe",
  "spanish": "equipo"
}

project_urls = {
  "english": "project",
  "portuguese": "projeto",
  "french": "projet",
  "spanish": "proyecto"
}

@bp.route('/')
@bp.route('/index.html')
def index():
  
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/index.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{honesty_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{honesty_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def honesty():
        
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/honesty.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{faqs_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{faqs_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def faqs():
        
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/faqs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{certificate_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{certificate_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def certificate():
        
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/certificate.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{syllabus_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{syllabus_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def syllabus():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/syllabus.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{staff_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{staff_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def staff():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/staff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{project_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{project_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )
