# -*- coding: utf-8 -*-


from app.blueprint_ext import Blueprint
from .api import Third


def get_urls(app):
    bp = Blueprint('third', __name__)
    bp.add_url_rule('thi/', view_func=Third.as_view('thi'))
    return bp
