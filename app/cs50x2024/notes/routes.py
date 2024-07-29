from flask import render_template
from . import notes_bp as bp
import os
import markdown


@bp.route('/0')
@bp.route('/0.html')
def notes0():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/0.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/1')
@bp.route('/1.html')
def notes1():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/1.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/2')
@bp.route('/2.html')
def notes2():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/2.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/3')
@bp.route('/3.html')
def notes3():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/3.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/4')
@bp.route('/4.html')
def notes4():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/4.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/5')
@bp.route('/5.html')
def notes5():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/5.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/6')
@bp.route('/6.html')
def notes6():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/6.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/7')
@bp.route('/7.html')
def notes7():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/7.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/8')
@bp.route('/8.html')
def notes8():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/8.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/9')
@bp.route('/9.html')
def notes9():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/9.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )


@bp.route('/10')
@bp.route('/10.html')
def notes10():
    with open(f"app/cs50x2024/content/{os.environ['COURSE_LANGUAGE']}/notes/10.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'cs50x2024/index.html',
        markdown_text=markdown.markdown(
            markdown_text, extensions=['tables'], tab_length=2)
    )
