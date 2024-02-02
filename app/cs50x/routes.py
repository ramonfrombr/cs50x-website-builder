from flask import render_template
from . import cs50x as bp
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

thanks_urls = {
  "english": "thanks",
  "portuguese": "obrigado",
  "french": "merci",
  "spanish": "gracias"
}

seminars_urls = {
  "english": "seminars",
  "portuguese": "seminarios",
  "french": "seminaires",
  "spanish": "seminarios"
}

sections_urls = {
  "english": "sections",
  "portuguese": "secoes",
  "french": "sections",
  "spanish": "secciones"
}

office_hours_urls = {
  "english": "office_hours",
  "portuguese": "tutorias",
  "french": "tutorials",
  "spanish": "gracias"
}

@bp.route('/')
@bp.route('/index.html')
def index():
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'index.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{honesty_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{honesty_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def honesty():
        
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/honesty.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{faqs_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{faqs_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def faqs():
        
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/faqs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{certificate_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{certificate_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def certificate():
        
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/certificate.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{syllabus_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{syllabus_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def syllabus():

    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/syllabus.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{staff_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{staff_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def staff():
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/staff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{project_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{project_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def project():
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{thanks_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{thanks_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def thanks():
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/thanks.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{seminars_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{seminars_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def seminars():

    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/seminars.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{sections_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{sections_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def sections():
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/sections.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f'/{office_hours_urls[os.environ["COURSE_LANGUAGE"]]}')
@bp.route(f'/{office_hours_urls[os.environ["COURSE_LANGUAGE"]]}.html')
def office_hours():
    with open(f"app/cs50x/content/{os.environ['COURSE_LANGUAGE']}/office_hours.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
