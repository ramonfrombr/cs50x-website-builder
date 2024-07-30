from flask import render_template
from . import pset1_bp as bp
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
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/1.html',
    )


@bp.route(f"/{URLS['world']}/")
@bp.route(f"/{URLS['world']}.html")
def world():

    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/world.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['me']}/")
@bp.route(f"/{URLS['me']}.html")
def me():

    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/me.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['mario_less']}/")
@bp.route(f"/{URLS['mario_less']}.html")
def mario_less():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/mario_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['mario_more']}/")
@bp.route(f"/{URLS['mario_more']}.html")
def mario_more():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/mario_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['cash']}/")
@bp.route(f"/{URLS['cash']}.html")
def cash():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/cash.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['credit']}/")
@bp.route(f"/{URLS['credit']}.html")
def credit():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/credit.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
