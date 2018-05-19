#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
main.py
helmetica main script
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-04-24'
import os
import click
from helmetica.scaffold.app import App
from helmetica.scaffold.config import Config
from helmetica.scaffold.wsgi import WSGI
from helmetica.scaffold.api import API
from helmetica.scaffold.test import Test
from helmetica.scaffold.docker import Docker
from helmetica.scaffold.extension import Extension
from helmetica.scaffold.pipfile import Pipfile

@click.group()
def main():
    pass

@main.command()
@click.option('--db', default=None, type=click.Choice(['sqlalchemy', 'mongoengine']), help='SQLAlchemy or Mongoengine or None')
@click.option('--cache', default=None, type=click.Choice(['redis', 'memcached']), help='Redis or Memd or None')
@click.option('--api', default=None, type=click.Choice(['restful', 'decorator', 'class']), help='Flask-Restful or Flask decorator or methodview')
@click.option('--web', default='gunicorn', help='use gunicorn or others')
@click.option('--virtualization', default=None, type=click.Choice(['docker', 'vagrant']), help='container or VM')
def init(db, cache, api, web, virtualization):
    dirs = ['./app/', './test/', './config/', './app/api/v1/']
    for dir in dirs:
        if os.path.exists(os.path.dirname(dir)):
            click.echo('[WARNING] directory {} is already exists, skip to create this directory'.format(dir))
            continue
        os.makedirs(os.path.dirname(dir))

    app = App(db=db, cache=cache, api=api)
    pipfile = Pipfile(db=db, cache=cache)
    wsgi = WSGI()
    config = Config()
    test = Test()
    docker = Docker(db=db, cache=cache)
    extension = Extension(db=db, cache=cache)
    api = API(api=api, name='root')

    with open('./Pipfile', 'w') as f:
        f.write(pipfile.create_pipfile())
        pipfile.lock()

    with open('app/__init__.py', 'w') as f:
        f.write(app.create_app__init__())

    with open('wsgi.py', 'w') as f:
        f.write(wsgi.create_wsgi())

    with open('config/__init__.py', 'w') as f:
        f.write(config.create_config(name='config', env='test'))
    with open('config/development.py', 'w') as f:
        f.write(config.create_config(name='development', env='development'))
    with open('config/production.py', 'w') as f:
        f.write(config.create_config(name='production', env='production'))

    with open('Dockerfile', 'w') as f:
        f.write(docker.create_dockerfile())
    with open('docker-compose.yml', 'w') as f:
        f.write(docker.create_docker_compose_yml())

    if extension.any_extension:
        with open('app/extensions.py', 'w') as f:
            f.write(extension.create_extensions())
    with open('test/__init__.py', 'w') as f:
        f.write(test.create__init__())
    with open('nose.cfg', 'w') as f:
        f.write(test.create_nose_cfg())

    with open('app/api/__init__.py', 'w') as f:
        f.write(api.create_restful__init__())
    with open('app/api/v1/__init__.py', 'w') as f:
        pass
    with open('app/api/v1/root.py', 'w') as f:
        f.write(api.create_restful())

@main.command()
@click.argument('name', type=str, required=True)
@click.option('--api', default=None, type=click.Choice(['restful', 'decorator', 'class']), help='Flask-Restful or Flask decorator or methodview')
@click.option('--version', default='v1', help='API version')
def api(name, api, version):
    path = 'app/api/{}/{}.py'.format(version, name)
    api = API(api=api, name=name)
    with open(path, 'w') as f:
        f.write(api.create_restful())

@main.command()
@click.argument('name', type=str, required=True)
@click.option('--db', default=None, type=click.Choice(['sqlalchemy', 'mongoengine']), help='SQLAlchemy or Mongoengine or None')
def model(name):
    # モデルを勝手に作成出来るようにしたい
    click.echo('create model {}'.format(name))
    pass
