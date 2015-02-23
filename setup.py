# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io


def read(*filenames, **kwargs):
    """
    From http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
    """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


setup(
    name="liu",
    version='1.1.1',
    description=read('DESCRIPTION.md'),
    long_description=read('README.md'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='LiU',
    author='Olle Vidner',
    author_email='olle@vidner.se',
    url="https://github.com/ovidner/python-liu",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
)
