from flask import Flask


def app_init():
    _app = Flask(__name__)

    from .urls import get_urls as api_get_urls
    _app.register_blueprint(api_get_urls(_app), url_perfiex='/api/')

    return _app
