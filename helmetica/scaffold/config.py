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
from inflector import Inflector


class Config(object):
    """ Config Scaffold
    """

    def  __init__(self, db=None, cache=None):
        self.db = db
        self.cache = cache

    def create_config(self, name='config', env='test'):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-

        class {name}(object):
            ENV = '{env}'
        """.format(
            name=Inflector().camelize(name),
            env=env
        )
        return dedent(source_code)
