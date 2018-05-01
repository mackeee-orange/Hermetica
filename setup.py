#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
setup.py
setup script
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-04-24'
from setuptools import setup

#with open('README.md', 'rt', encoding='utf8') as f:
#    readme = f.read()

setup(
    name='Helmetica',
    version='0.0.1',
    description='scaffold command line interface for Flask application',
    #long_description=readme,
    author='Yoshiya Ito',
    author_email='myon53@gmail.com',
    url='https://github.com/yoshiya0503/Flask-Best-Practices.git',
    license='MIT',
    platforms='any',
    packages=['helmetica', 'helmetica.scaffold'],
    install_requires=[
        'click>=5.1',
        'Inflector>=2.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points='''
        [console_scripts]
        helmetica=helmetica.cli:main
    '''
)
