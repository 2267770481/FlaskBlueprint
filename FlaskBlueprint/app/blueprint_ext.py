# -*- coding: utf-8 -*-
from flask import Blueprint as _Blueprint

class Blueprint(_Blueprint):

    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            url_prefix = options.pop('url_prefix', None)
            if url_prefix is None:
                url_prefix = blueprint.url_prefix
            if state.url_prefix:
                url_prefix = state.url_prefix + url_prefix

            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)

        self.record(deferred)
