from app.blueprint_ext import Blueprint
import importlib


def get_urls(app):
    bp = Blueprint('api', 'api')

    api_modules = {
        'first': 'first/',
        'second': 'second/',
        'third': 'third/'
    }

    for module, path in api_modules.items():
        m = importlib.import_module('.' + module, package='app.api')
        urls = m.get_urls(app)
        if urls:
            bp.register_blueprint(urls, url_prefix=path)

    return bp
