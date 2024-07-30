from flask import render_template
from . import pset2_bp as bp
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
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/2.html',
    )


@bp.route(f"/{URLS['scrabble']}/")
@bp.route(f"/{URLS['scrabble']}.html")
def scrabble():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/scrabble.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['readability']}/")
@bp.route(f"/{URLS['readability']}.html")
def readability():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/readability.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['caesar']}/")
@bp.route(f"/{URLS['caesar']}.html")
def caesar():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/caesar.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['substitution']}/")
@bp.route(f"/{URLS['substitution']}.html")
def substitution():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/substitution.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
