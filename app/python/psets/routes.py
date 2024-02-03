from flask import Blueprint, render_template
from . import psets_bp as bp
import marko
import os
from flask import current_app

@bp.route('/')
@bp.route('/index.html')
def psets():
   return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/index.html',
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/0')
@bp.route('/0.html')
def pset0():
   return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/0.html',
    )

@bp.route('/0/pset0_project/')
@bp.route('/0/pset0_project.html')
def pset0_project():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset0_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/1')
@bp.route('/1.html')
def pset1():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/1.html',
    )

@bp.route(f"/1/pset1_project/")
@bp.route(f"/1/pset1_project.html")
def pset1_project():
    
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset1_project.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/2')
@bp.route('/2.html')
def pset2():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/2.html',
    )

@bp.route(f"/2/pset2_project/")
@bp.route(f"/2/pset2_project.html")
def pset2_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset2_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/3')
@bp.route('/3.html')
def pset3():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/3.html',
    )

@bp.route(f"/3/pset3_project/")
@bp.route(f"/3/pset3_project.html")
def pset3_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset3_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/4')
@bp.route('/4.html')
def pset4():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/4.html',
    )

@bp.route(f"/4/pset4_project")
@bp.route(f"/4/pset4_project.html")
def pset4_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset4_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/5')
@bp.route('/5.html')
def pset5():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/5.html',
    )
    
@bp.route(f"/5/pset5_project/")
@bp.route(f"/5/pset5_project.html")
def pset5_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset5_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/6')
@bp.route('/6.html')
def pset6():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/6.html',
    )

@bp.route(f"/6/pset6_project/")
@bp.route(f"/6/pset6_project.html")
def pset6_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset6_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/7')
@bp.route('/7.html')
def pset7():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/7.html',
    )

@bp.route(f"/7/pset7_project/")
@bp.route(f"/7/pset7_project.html")
def pset7_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset7_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/8/')
@bp.route('/8.html')
def pset8():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/8.html',
    )
    
@bp.route(f"/8/pset8_project/")
@bp.route(f"/8/pset8_project.html")
def pset8_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset8_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
   
#############################################################################
#############################################################################
#############################################################################

@bp.route('/9')
@bp.route('/9.html')
def pset9():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/9.html',
    )

@bp.route(f"/9/pset9_project/")
@bp.route(f"/9/pset9_project.html")
def pset9_project():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pset9_project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
