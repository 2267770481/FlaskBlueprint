# -*- coding: utf-8 -*-


from app.blueprint_ext import Blueprint
from .api import First


def get_urls(app):
    bp = Blueprint('first', __name__)
    bp.add_url_rule('first/', view_func=First.as_view('first'))
    return bp
