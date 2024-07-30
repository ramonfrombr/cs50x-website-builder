from flask import render_template
from . import pset6_bp as bp
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
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/6.html',
    )


@bp.route(f"/{URLS['python_hello']}/")
@bp.route(f"/{URLS['python_hello']}.html")
def python_hello():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_hello.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['python_mario_less']}/")
@bp.route(f"/{URLS['python_mario_less']}.html")
def python_mario_less():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_mario_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['python_mario_more']}/")
@bp.route(f"/{URLS['python_mario_more']}.html")
def python_mario_more():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_mario_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['python_cash']}/")
@bp.route(f"/{URLS['python_cash']}.html")
def python_cash():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_cash.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['python_credit']}/")
@bp.route(f"/{URLS['python_credit']}.html")
def python_credit():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_credit.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['python_readability']}/")
@bp.route(f"/{URLS['python_readability']}.html")
def python_readability():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_readability.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route(f"/{URLS['dna']}/")
@bp.route(f"/{URLS['dna']}.html")
def dna():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/dna.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
