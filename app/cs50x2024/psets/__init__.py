from flask import Blueprint
from .pset0 import pset0_bp
from .pset1 import pset1_bp
from .pset2 import pset2_bp
from .pset3 import pset3_bp
from .pset4 import pset4_bp
from .pset5 import pset5_bp
from .pset6 import pset6_bp
from .pset7 import pset7_bp
from .pset8 import pset8_bp
from .pset9 import pset9_bp

psets_bp = Blueprint(
    'psets',
    __name__,
    template_folder='templates'
)

psets_bp.register_blueprint(pset0_bp, url_prefix='/0')
psets_bp.register_blueprint(pset1_bp, url_prefix='/1')
psets_bp.register_blueprint(pset2_bp, url_prefix='/2')
psets_bp.register_blueprint(pset3_bp, url_prefix='/3')
psets_bp.register_blueprint(pset4_bp, url_prefix='/4')
psets_bp.register_blueprint(pset5_bp, url_prefix='/5')
psets_bp.register_blueprint(pset6_bp, url_prefix='/6')
psets_bp.register_blueprint(pset7_bp, url_prefix='/7')
psets_bp.register_blueprint(pset8_bp, url_prefix='/8')
psets_bp.register_blueprint(pset9_bp, url_prefix='/9')
