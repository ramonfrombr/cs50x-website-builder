from . import cs50x2024 as bp
from flask import render_template
import os
import markdown


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


@bp.route('/honesty')
@bp.route('/honesty.html')
def honesty():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/honesty.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/certificate')
@bp.route('/certificate.html')
def certificate():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/certificate.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/faqs')
@bp.route('/faqs.html')
def faqs():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/faqs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/staff')
@bp.route('/staff.html')
def staff():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/staff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/syllabus')
@bp.route('/syllabus.html')
def syllabus():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/syllabus.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/project')
@bp.route('/project.html')
def project():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
