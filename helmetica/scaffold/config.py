#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
config.py
scaffold create_config
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-05-01'
from textwrap import dedent


class Config(object):
    """ Config Scaffold
    """

    def  __init__(self, db=None, cache=None):
        self.db = db
        self.cache = cache

    def create__init__(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-

        class Config(object):
            FLASK_ENV = 'development'
        """
        return dedent(source_code)
