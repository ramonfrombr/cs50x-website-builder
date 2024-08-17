import os
from flask import render_template
from . import weeks_bp as bp
from ..content.english.language import week_page as english_week_page
from ..content.spanish.language import week_page as spanish_week_page
from ..content.french.language import week_page as french_week_page
from ..content.portuguese.language import week_page as portuguese_week_page
from ..content.english.language import weeks as english_weeks
from ..content.spanish.language import weeks as spanish_weeks
from ..content.french.language import weeks as french_weeks
from ..content.portuguese.language import weeks as portuguese_weeks


if os.environ['COURSE_LANGUAGE'] == 'english':
    weeks_content = {
        "week_page": english_week_page,
        "weeks": english_weeks
    }
elif os.environ['COURSE_LANGUAGE'] == 'spanish':
    weeks_content = {
        "week_page": spanish_week_page,
        "weeks": spanish_weeks
    }
elif os.environ['COURSE_LANGUAGE'] == 'french':
    weeks_content = {
        "week_page": french_week_page,
        "weeks": french_weeks
    }
elif os.environ['COURSE_LANGUAGE'] == 'portuguese':
    weeks_content = {
        "week_page": portuguese_week_page,
        "weeks": portuguese_weeks
    }


@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('cs50x2024/weeks/index.html')


@bp.route('/0')
@bp.route('/0.html')
def week0():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["0"]
    )


@bp.route('/1')
@bp.route('/1.html')
def week1():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["1"]
    )


@bp.route('/2')
@bp.route('/2.html')
def week2():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["2"]
    )


@bp.route('/3')
@bp.route('/3.html')
def week3():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["3"]
    )


@bp.route('/4')
@bp.route('/4.html')
def week4():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["4"]
    )


@bp.route('/5')
@bp.route('/5.html')
def week5():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["5"]
    )


@bp.route('/6')
@bp.route('/6.html')
def week6():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["6"]
    )


@bp.route('/7')
@bp.route('/7.html')
def week7():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["7"]
    )


@bp.route('/8')
@bp.route('/8.html')
def week8():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["8"]
    )


@bp.route('/9')
@bp.route('/9.html')
def week9():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["9"]
    )


@bp.route('/10')
@bp.route('/10.html')
def week10():
    return render_template(
        'cs50x2024/weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["weeks"]["10"]
    )
