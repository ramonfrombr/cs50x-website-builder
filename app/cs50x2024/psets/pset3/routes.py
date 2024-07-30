from flask import render_template
from . import pset3_bp as bp
import markdown
import os
from ...content.english.language import psets_urls as english_psets_url
from ...content.spanish.language import psets_urls as spanish_psets_url
from ....types import PagesUrlsType

URLS: PagesUrlsType = english_psets_url

if os.environ['COURSE_LANGUAGE'] == 'spanish':
    URLS = spanish_psets_url


@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template(
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/3.html',
    )


@bp.route(f"/{URLS['sort']}/")
@bp.route(f"/{URLS['sort']}.html")
def sort():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/sort.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['plurality']}/")
@bp.route(f"/{URLS['plurality']}.html")
def plurality():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/plurality.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['runoff']}/")
@bp.route(f"/{URLS['runoff']}.html")
def runoff():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/runoff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['tideman']}/")
@bp.route(f"/{URLS['tideman']}.html")
def tideman():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/tideman.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
