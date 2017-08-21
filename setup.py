#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Chris Ward <cward@redhat.com>

from setuptools import setup

long_description = '''Scripts for grabbing audio from youtube'''

setup_info = dict(
    # Metadata
    name='grabit',
    version='0.01',
    license='MIT',
    author='Chris Ward',
    author_email='kejbaly2@gmail.com',
    description=long_description,
    long_description=long_description,
    url='https://github.com/kejbaly2/grabit',
    # Package info
    packages=['grabit'],
    install_requires=[
    ],
    scripts=['bin/grabit'],
)


setup(**setup_info)
