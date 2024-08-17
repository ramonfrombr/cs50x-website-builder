from flask import render_template
from . import core as bp


@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('cs50x2024/redirect.html')
