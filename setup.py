from setuptools import setup

requirements = ['termcolor']
description = 'A color coded, tagged print statement replacement'
long_description = 'This package is designed to act as a replacement for the built in Python 3 print statement. It prints color coded, tagged messages that can be useful in debugging, or if you just prefer a cleaner appearance in your terminal.'
setup(name='PrintTags', version='1.0', scripts=['PrintTags'], install_requires=requirements)