#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
test.py
Test Scaffold
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-04-27'


class Test(object):

    def create__init__(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-

        import json
        from contextlib import contextmanager
        from unittest import TestCase
        from app import create_app

        app = create_app()

        class Experiment(TestCase):

            def setUp(self):
                app.testing = True
                self.client = app.test_client()
                self.logger = app.logger
                self.app_config = app.config
                self.app_context = app.app_context()
                self.app_context.push()

            def tearDown(self):
                self.app_context.pop()

            def response_to_dict(self, response):
                return json.loads(response.data)

            @contextmanager
            def authenticate(self, user=None):
                pass
        """
        return source_code

    def create_nose_cfg(self):
        source_code = """\
        [nosetests]
        verbosity=2
        with-timer=1
        rednose=True
        nocapture=True
        with-coverage=1
        cover-package=.
        """
        return source_code
