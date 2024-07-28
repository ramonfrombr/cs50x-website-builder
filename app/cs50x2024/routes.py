from . import cs50x2024 as bp
from flask import render_template
import marko
import os


@bp.route('/')
@bp.route('/index.html')
def index():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=marko.convert(markdown_text)
    )
