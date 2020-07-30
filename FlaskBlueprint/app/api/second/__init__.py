# -*- coding: utf-8 -*-
from app.blueprint_ext import Blueprint
from .api import Second


def get_urls(app):
    bp = Blueprint('second', __name__)
    bp.add_url_rule('second/', view_func=Second.as_view('second'), methods=('GET', ))
    return bp
