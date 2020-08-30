# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import PrintTags

name = 'PrintTags'
description = 'A lightweight, tagged, and color-coded Python 3 print alternative'
long_description = (
    'PrintTags is a lightweight package designed to act as an '
    'alternative to the built-in Python 3.6+ print function. It prints '
    'color coded, tagged messages that can be useful in debugging, '
    'or if you just prefer a cleaner appearance in your terminal.'
)
url = 'https://github.com/mdlockyer/PrintTags'
author = 'Michael Lockyer'
author_email = 'mdlockyer@gmail.com'
version = PrintTags.__version__
license = 'MIT License'
classifiers = (
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Intended Audience :: Developers',
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
)
package_data = {'PrintTags': ['py.typed']}
packages = find_packages()
zip_safe = False

setup(name=name, description=description, long_description=long_description,
      version=version, url=url, author=author, author_email=author_email,
      license=license, classifiers=classifiers, package_data=package_data,
      packages=packages, zip_safe=zip_safe)
