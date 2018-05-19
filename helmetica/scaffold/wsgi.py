#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
wsgi.py
scaffold create_wsgi
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-05-01'
from textwrap import dedent


class WSGI(object):
    """ wsgi Scaffold
    """

    def create_wsgi(self):
        source_code = """
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        import os
        from app import create_app

        app = create_app(os.getenv('FLASK_ENV', None))

        if __name__ == '__main__':
            app.run(host='0.0.0.0')
        """
        return dedent(source_code).strip()
