#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
api.py
scaffold create_api
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-05-01'
from textwrap import dedent
from inflector import Inflector


class API(object):
    """ API Scaffold
    """

    def __init__(self, api=None, name=None):
        self.api = api
        self.name = name

    def create_restful__init__(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        from flask import Blueprint
        from flask_restful import Api
        from app.api.v1.root import Root

        api_v1 = Blueprint('api/v1', __name__)
        api = Api(api_v1)
        api.add_resource(Root, '/')
        """
        return dedent(source_code)

    def create_restful(self):
        source_code = """\
        #! /usr/bin/env python3
        # -*- encoding: utf-8 -*-
        from flask_restful import Resource, fields, marshal_with, reqparse

        resource_field = {{
            'id': fields.Integer,
            'created_at': fields.DateTime,
            'updated_at': fields.DateTime,
        }}

        class {name}(Resource):
            parser = reqparse.RequestParser()
            parser.add_argument('query', type=str, help="query string")
            parser.add_argument('body', type=str, help="body string")

            @marshal_with(resource_fields)
            def get(self, id=None):
                args = self.post_parser.parse_args()
                if id is None:
                    return {{}}, 200
                return [], 200

            @marshal_with(resource_fields)
            def post(self):
                args = self.post_parser.parse_args()
                return {{}}, 201

            @marshal_with(resource_fields)
            def put(self, id=None):
                args = self.post_parser.parse_args()
                return {{}}, 204

            @marshal_with(resource_fields)
            def delete(self, id=None):
                return {{}}, 204
        """.format(
            name=Inflector().camelize(self.name)
        )
        return dedent(source_code)
