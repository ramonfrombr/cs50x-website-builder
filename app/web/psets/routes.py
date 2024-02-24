from flask import Blueprint, render_template
from . import psets_bp as bp
import marko
import os
from flask import current_app

@bp.route('/')
@bp.route('/index.html')
def psets():
   return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/index.html',
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/0')
@bp.route('/0.html')
def pset0():
   return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/0.html',
    )

@bp.route('/0/search/')
@bp.route('/0/search.html')
def search():

    with open(f"app/web/content/{os.environ['COURSE_LANGUAGE']}/specifications/search.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'web/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/1')
@bp.route('/1.html')
def pset1():
    return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/1.html',
    )

@bp.route(f"/1/wiki/")
@bp.route(f"/1/wiki.html")
def wiki():
    
    with open(f"app/web/content/{os.environ['COURSE_LANGUAGE']}/specifications/wiki.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'web/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/2')
@bp.route('/2.html')
def pset2():
    return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/2.html',
    )

@bp.route(f"/2/commerce/")
@bp.route(f"/2/commerce.html")
def commerce():
    with open(f"app/web/content/{os.environ['COURSE_LANGUAGE']}/specifications/commerce.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'web/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/3')
@bp.route('/3.html')
def pset3():
    return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/3.html',
    )

@bp.route(f"/3/mail/")
@bp.route(f"/3/mail.html")
def mail():
    with open(f"app/web/content/{os.environ['COURSE_LANGUAGE']}/specifications/mail.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'web/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/4')
@bp.route('/4.html')
def pset4():
    return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/4.html',
    )

@bp.route(f"/4/network")
@bp.route(f"/4/network.html")
def network():
    with open(f"app/web/content/{os.environ['COURSE_LANGUAGE']}/specifications/network.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'web/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/5')
@bp.route('/5.html')
def pset5():
    return render_template(
        f'web/{os.environ["COURSE_LANGUAGE"]}/psets/5.html',
    )
    
@bp.route(f"/5/capstone/")
@bp.route(f"/5/capstone.html")
def capstone():
    with open(f"app/web/content/{os.environ['COURSE_LANGUAGE']}/specifications/capstone.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'web/blank.html',
        markdown_text=marko.convert(markdown_text)
    )
