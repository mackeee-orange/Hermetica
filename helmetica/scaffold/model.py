#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
model.py
scaffold model
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-04-27'
from textwrap import dedent
from inflector import Inflector


class Model(object):
    """ Model Scaffold
    """

    def __init__(self, db):
        self.db = db

    def create_sqlalchemy__init__(self):
        source_code = """
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        from datetime import datetime
        from sqlalchemy.ext.declarative import declared_attr
        from app.extensions import db


        class Model(db.Model):
            __abstract__ = True

            id = db.Column(db.Integer, primary_key=True)

            @declared_attr
            def created_at(cls):
                return db.Column(db.DateTime, default=datetime.utcnow)

            @declared_attr
            def updated_at(cls):
                return db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        """
        return dedent(source_code).strip()

    def create_sqlalchmey_model(self):
        pass

    def create_mongoengine__init__(self):
        pass

    def create_mongoengine__model(self):
        pass
