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
from helmetica.scaffold.extension import Extension

@click.group()
def main():
    pass

@main.command()
@click.option('--db', default=None, help='SQLAlchemy or Mongoengine or None')
@click.option('--cache', default=None, help='Redis or Memd or None')
@click.option('--restful', default=None, help='use Flask-Restful or API based on Flask common decorator')
@click.option('--web', default='gunicorn', help='use gunicorn or others')
def init(db, cache, restful, web):
    dirs = ['./app/', './test/', './config/']
    for dir in dirs:
        if os.path.exists(os.path.dirname(dir)):
            click.echo('[WARNING] directory {} is already exists, skip to create this directory'.format(dir))
            continue
        os.makedirs(os.path.dirname(dir))
    app = App(db=db, cache=cache)
    extension = Extension(db=db, cache=cache)
    with open('app/__init__.py', 'w') as __init__:
        __init__.write(app.create_app__init__())
    if extension.any_extension:
        with open('app/extensions.py', 'w') as ext:
            ext.write(extension.create_extensions())
    with open('wsgi.py', 'w') as wsgi:
        wsgi.write(app.create_wsgi())
    with open('config/__init__.py', 'w') as config:
        config.write(app.create_config())
    # 最初にディレクトリを作成して欲しい。
    # database を SQLAlchemy, Mongoengine, None を指定出来るようにしたい
    # cache を redis, memcached, None を指定できるようにしたい
    # 初回いきなり起動できるscaffold にしたい

@main.command()
@click.argument('name', type=str, required=True)
@click.option('--version', default='v1', help='API version')
def api(name, version):
    # API を勝手に作成出来るようにしたい
    click.echo('create api {}/{}'.format(name, version))
    pass

@main.command()
@click.argument('name', type=str, required=True)
def model(name):
    # モデルを勝手に作成出来るようにしたい
    click.echo('create model {}'.format(name))
    pass
