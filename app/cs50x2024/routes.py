from . import cs50x2024 as bp
from flask import render_template
import os
import markdown
from .content.english.language import pages_url as english_pages_url
from .content.spanish.language import pages_url as spanish_pages_url
from ..types import PagesUrlsType

URLS: PagesUrlsType = english_pages_url

if os.environ['COURSE_LANGUAGE'] == 'spanish':
    URLS = spanish_pages_url


@bp.route('/')
@bp.route('/index.html')
def index():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['honesty']}")
@bp.route(f"/{URLS['honesty']}.html")
def honesty():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/honesty.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['certificate']}")
@bp.route(f"/{URLS['certificate']}.html")
def certificate():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/certificate.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['faqs']}")
@bp.route(f"/{URLS['faqs']}.html")
def faqs():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/faqs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['staff']}")
@bp.route(f"/{URLS['staff']}.html")
def staff():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/staff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['syllabus']}")
@bp.route(f"/{URLS['syllabus']}.html")
def syllabus():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/syllabus.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['project']}")
@bp.route(f"/{URLS['project']}.html")
def project():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['style']}")
@bp.route(f"/{URLS['style']}.html")
def style():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/style.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
