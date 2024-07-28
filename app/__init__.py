from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .cs50x2024 import cs50x2024
        app.register_blueprint(cs50x2024, url_prefix="/2024")

    return app