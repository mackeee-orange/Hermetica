#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
app.py
scaffold create_app
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-04-27'
from textwrap import dedent


class App(object):
    """ App Scaffold
    """

    def __init__(self, api=None, db=None, cache=None):
        self.db = db
        self.cache = cache
        self.api = api

    def create_app__init__(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        from flask import Flask
        {}

        def create_app(env='development'):
            app = Flask(__name__)

            if env == 'development':
                app.config.from_object('config.development.Development')
            elif env == 'production':
                app.config.from_object('config.production.Production')
            else:
                app.config.from_object('config.development.Development')

            {}
            {}

            return app
        """.format(
            self.create_header(),
            self.create_extension(),
            self.create_api(),
        )
        return dedent(source_code)

    def create_header(self):
        import_db = ''
        import_cache = ''
        import_api = ''
        if self.db == 'sqlalchemy' or self.db == 'mongoengine':
            import_db = 'from app.extensions import db'
        if self.cache == 'redis':
            import_cache = 'from app.extensions import redis'
        if self.api:
            import_api = 'from app.api import api_v1'

        header = """
        {}
        {}
        {}
        """.format(import_db, import_cache, import_api)
        return header.strip()

    def create_extension(self):
        source_code = """\
            {db}
            {cache}
        """.format(
            db=self.create_db(),
            cache=self.create_cache(),
        ).strip()
        return source_code

    def create_db(self):
        if self.db:
            return 'db.init_app(app)'
        else:
            return ''

    def create_cache(self):
        if self.cache:
            return 'redis.init_app(app)'
        else:
            return ''

    def create_api(self):
        if self.api:
            return "app.register_blueprint(api_v1, url_prefix='/api/v1')"
        else:
            return ''
