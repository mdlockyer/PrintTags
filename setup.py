# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import PrintTags

name = 'PrintTags'
description = 'A color coded, tagged Python 3 print statement replacement'
long_description = (
    'PrintTags is a lightweight package designed to act as an '
    'alternative to the built-in Python 3 print function. It prints '
    'color coded, tagged messages that can be useful in debugging, '
    'or if you just prefer a cleaner appearance in your terminal.'
)
url = 'https://github.com/MichaelDylan77/PrintTags'
author = 'Michael Lockyer'
author_email = 'mdlockyer@gmail.com'
version = PrintTags.__version__
license = 'MIT License'
classifiers = (
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
)
packages = find_packages()

setup(name=name, description=description, long_description=long_description,
      version=version, url=url, author=author, author_email=author_email,
      license=license, classifiers=classifiers, packages=packages)
