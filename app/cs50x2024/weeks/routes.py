from flask import render_template
from . import weeks_bp as bp


@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('cs50x2024/weeks/index.html')
