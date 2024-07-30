from flask import render_template
from . import pset4_bp as bp
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
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/4.html',
    )


@bp.route(f"/{URLS['volume']}")
@bp.route(f"/{URLS['volume']}.html")
def volume():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/volume.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['filter_less']}/")
@bp.route(f"/{URLS['filter_less']}.html")
def filter_less():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/filter_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['filter_more']}/")
@bp.route(f"/{URLS['filter_more']}.html")
def filter_more():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/filter_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['recover']}/")
@bp.route(f"/{URLS['recover']}.html")
def recover():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/recover.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
