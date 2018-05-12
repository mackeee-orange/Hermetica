#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
docker.py
scaffold create_docker
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-05-01'
from textwrap import dedent


class Docker(object):
    """ Docker Scaffold
    """

    def __init__(self, db=None, cache=None):
        self.db = db
        self.cache = cache

    def create_dockerfile(self):
        source_code = """\
        FROM python:3.6
        # -- Install Pipenv:
        RUN pip install pipenv --upgrade
        WORKDIR /tmp
        # -- Adding Pipfiles
        ADD ./Pipfile Pipfile
        ADD ./Pipfile.lock Pipfile.lock
        RUN pipenv install --deploy --system
        """
        return dedent(source_code)

    def create_docker_compose_yml(self):
        source_code = """\
        version: '3'
        services:
          api:
            build: .
            volumes:
              - .:/app
            working_dir: "/app"
            environment:
              FLASK_APP: "wsgi.py"
              FLASK_DEBUG: "1"
            command: "flask run --host=0.0.0.0"
            links:
              - redis
              - db
            ports:
              - "5000:5000"
          {db}
          {cache}
        """.format(
            db=self.create_db(),
            cache=self.create_cache(),
        )
        return dedent(source_code).strip()

    def create_db(self):
        source_code = ''
        if self.db == 'sqlalchemy':
            source_code = """db:
              image: mysql:5.7
              command: mysqld --character-set-server=utf8mb4 --collation-server=utf8mb4_general_ci
              environment:
                MYSQL_DATABASE: "app_development"
                MYSQL_ROOT_PASSWORD: "root"
              expose:
                - "3306"
            """
        if self.db == 'mongoengine':
            source_code = """db:
              image: mongo:latest
              expose:
                - "27017"
              command: mongod --smallfiles --logpath=/dev/null
            """
        return dedent(source_code)

    def create_cache(self):
        source_code = ''
        if self.cache == 'redis':
            source_code = """redis:
              image: redis:3.2
              expose:
                - "6379"
            """
        return dedent(source_code)
