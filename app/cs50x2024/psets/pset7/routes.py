from flask import render_template
from . import pset7_bp as bp
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
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/7.html',
    )


@bp.route(f"/{URLS['songs']}/")
@bp.route(f"/{URLS['songs']}.html")
def songs():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/songs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['movies']}/")
@bp.route(f"/{URLS['movies']}.html")
def movies():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/movies.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['fiftyville']}/")
@bp.route(f"/{URLS['fiftyville']}.html")
def fiftyville():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/fiftyville.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
