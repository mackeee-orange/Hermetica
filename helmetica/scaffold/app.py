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

    def __init__(self, db=None, cache=None):
        self.db = db
        self.cache = cache

    def create_app__init__(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        from flask import Flask

        def create_app(env='development')
            app = Flask(__name__)
            if env == 'development':
                app.config.from_object('config.development.Development')
            elif env == 'production':
                app.config.from_object('config.production.Production')
            else:
                app.config.from_object('config.development.Development')

            {}
            return app
        """.format(
            self.create_extension()
        )
        return dedent(source_code)

    def create_wsgi(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        import os
        from app import create_app

        app = create_app(os.getenv('FLASK_ENV', None))

        if __name__ == '__main__':
            app.run(host='0.0.0.0')
        """
        return dedent(source_code)

    def create_config(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-

        class Config(object):
            FLASK_ENV = 'development'
        """
        return dedent(source_code)

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
