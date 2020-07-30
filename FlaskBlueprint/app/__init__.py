from flask import Flask

def init_app():
    _app = Flask(__name__)

    from .api.urls import get_urls as api_get_urls
    _app.register_blueprint(api_get_urls(_app), url_prefix='/api/')

    return _app

