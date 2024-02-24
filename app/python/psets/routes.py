from flask import Blueprint, render_template
from . import psets_bp as bp
import marko
import os
from flask import current_app

@bp.route('/')
@bp.route('/index.html')
def psets():
   return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/index.html',
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/0')
@bp.route('/0.html')
def pset0():
   return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/0.html',
    )

@bp.route('/0/einstein/')
@bp.route('/0/einstein.html')
def einstein():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/einstein.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/0/faces/')
@bp.route('/0/faces.html')
def faces():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/faces.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/0/indoor/')
@bp.route('/0/indoor.html')
def indoor():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/indoor.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/0/playback/')
@bp.route('/0/playback.html')
def playback():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/playback.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/0/tip/')
@bp.route('/0/tip.html')
def tip():

    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/tip.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/1')
@bp.route('/1.html')
def pset1():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/1.html',
    )

@bp.route(f"/1/bank/")
@bp.route(f"/1/bank.html")
def bank():
    
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/bank.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/deep/")
@bp.route(f"/1/deep.html")
def deep():
    
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/deep.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/extensions/")
@bp.route(f"/1/extensions.html")
def extensions():
    
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/extensions.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/interpreter/")
@bp.route(f"/1/interpreter.html")
def interpreter():
    
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/interpreter.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/meal/")
@bp.route(f"/1/meal.html")
def meal():
    
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/meal.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )


#############################################################################
#############################################################################
#############################################################################

@bp.route('/2')
@bp.route('/2.html')
def pset2():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/2.html',
    )

@bp.route(f"/2/camel/")
@bp.route(f"/2/camel.html")
def camel():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/camel.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/2/coke/")
@bp.route(f"/2/coke.html")
def coke():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/coke.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/2/nutrition/")
@bp.route(f"/2/nutrition.html")
def nutrition():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/nutrition.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/2/plates/")
@bp.route(f"/2/plates.html")
def plates():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/plates.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )
  
@bp.route(f"/2/twttr/")
@bp.route(f"/2/twttr.html")
def twttr():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/twttr.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/3')
@bp.route('/3.html')
def pset3():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/3.html',
    )

@bp.route(f"/3/fuel/")
@bp.route(f"/3/fuel.html")
def fuel():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/fuel.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/3/grocery/")
@bp.route(f"/3/grocery.html")
def grocery():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/grocery.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/3/outdated/")
@bp.route(f"/3/outdated.html")
def outdated():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/outdated.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/3/taqueria/")
@bp.route(f"/3/taqueria.html")
def taqueria():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/taqueria.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/4')
@bp.route('/4.html')
def pset4():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/4.html',
    )

@bp.route(f"/4/adieu/")
@bp.route(f"/4/adieu.html")
def adieu():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/adieu.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/bitcoin/")
@bp.route(f"/4/bitcoin.html")
def bitcoin():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/bitcoin.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/emojize/")
@bp.route(f"/4/emojize.html")
def emojize():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/emojize.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/figlet/")
@bp.route(f"/4/figlet.html")
def figlet():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/figlet.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )
  
@bp.route(f"/4/game/")
@bp.route(f"/4/game.html")
def game():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/game.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/professor/")
@bp.route(f"/4/professor.html")
def professor():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/professor.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/5')
@bp.route('/5.html')
def pset5():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/5.html',
    )
    
@bp.route(f"/5/test_bank/")
@bp.route(f"/5/test_bank.html")
def test_bank():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/test_bank.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/5/test_fuel/")
@bp.route(f"/5/test_fuel.html")
def test_fuel():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/test_fuel.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/5/test_plates/")
@bp.route(f"/5/test_plates.html")
def test_plates():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/test_plates.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/5/test_twttr/")
@bp.route(f"/5/test_twttr.html")
def test_twttr():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/test_twttr.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/6')
@bp.route('/6.html')
def pset6():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/6.html',
    )

@bp.route(f"/6/lines/")
@bp.route(f"/6/lines.html")
def lines():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/lines.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/pizza/")
@bp.route(f"/6/pizza.html")
def pizza():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/pizza.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/scourgify/")
@bp.route(f"/6/scourgify.html")
def scourgify():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/scourgify.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/shirt/")
@bp.route(f"/6/shirt.html")
def shirt():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/shirt.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/7')
@bp.route('/7.html')
def pset7():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/7.html',
    )

@bp.route(f"/7/numb3rs/")
@bp.route(f"/7/numb3rs.html")
def numb3rs():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/numb3rs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/7/response/")
@bp.route(f"/7/response.html")
def response():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/response.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/7/um/")
@bp.route(f"/7/um.html")
def um():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/um.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/7/watch/")
@bp.route(f"/7/watch.html")
def watch():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/watch.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/7/working/")
@bp.route(f"/7/working.html")
def working():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/working.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/8/')
@bp.route('/8.html')
def pset8():
    return render_template(
        f'python/{os.environ["COURSE_LANGUAGE"]}/psets/8.html',
    )
    
@bp.route(f"/8/jar/")
@bp.route(f"/8/jar.html")
def jar():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/jar.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/8/seasons/")
@bp.route(f"/8/seasons.html")
def seasons():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/seasons.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/8/shirtificate/")
@bp.route(f"/8/shirtificate.html")
def shirtificate():
    with open(f"app/python/content/{os.environ['COURSE_LANGUAGE']}/specifications/shirtificate.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'python/blank.html',
        markdown_text=marko.convert(markdown_text)
    )
