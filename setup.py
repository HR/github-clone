#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import codecs
import os
import re
from setuptools import find_packages, setup


version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('ghclone/ghclone.py',) as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        version = match.group(1)
    else:
        raise RuntimeError("No version number found!")


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


README = local_file('README.md')
long_description = codecs.open(README, encoding='utf-8').read()


setup(
    name='ghclone',
    packages=['ghclone'],
    version=version,
    description='A script for cloning any sub-directories of any GitHub repository',
    long_description=long_description,
    url='https://github.com/HR/github-clone',
    author='Habib Rehman',
    author_email='h@rehman.email',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'requests>=2.20.0',
        'docopt>=0.6.2',
    ],
    entry_points={
        'console_scripts': [
            'ghclone=ghclone.ghclone:main',
        ],
    },
)