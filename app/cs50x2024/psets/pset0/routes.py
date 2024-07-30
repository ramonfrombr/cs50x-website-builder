from flask import render_template
from . import pset0_bp as bp
import markdown
import os


@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template(
        f'cs50x2024/languages/{os.environ["COURSE_LANGUAGE"]}/psets/0.html',
    )


@bp.route('/scratch/')
@bp.route('/scratch.html')
def scratch():

    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/specifications/scratch.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
