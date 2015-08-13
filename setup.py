#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='multisnake',
    version='0.0.1',
    description='Massively Multiplayer Snake',
    long_description=readme,
    author='Eric Nelson',
    author_email='nelseric.alt@gmail.com',
    url='https://github.com/nelseric/multisnake',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        "console_scripts": [
            "multisnake-server = multisnake.network_server:start",
            "multisnake-client = multisnake.network_client:start"
        ]
    }
)
