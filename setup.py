#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from setuptools import find_packages, setup


version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('ghclone/__init__.py',) as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        version = match.group(1)
    else:
        raise RuntimeError('No version number found!')


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='github-clone',
    packages=find_packages(),
    version=version,
    description='Clone any subdirectory of a GitHub repo with just the GitHub URL',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HR/github-clone',
    author='Habib Rehman',
    author_email='Hi@HabibRehman.com',
    license='Apache 2.0',
    project_urls={
        "Bug Tracker": "https://github.com/HR/github-clone/issues",
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.20.0',
        'docopt>=0.6.2',
    ],
    entry_points={
        'console_scripts': [
            'ghclone=ghclone:main',
        ],
    },
)