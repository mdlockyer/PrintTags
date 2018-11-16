from setuptools import setup, find_packages

name = 'PrintTags'
description = 'A color coded, tagged Python 3 print statement replacement'
long_description = 'This package is designed to act as a replacement for the built in Python 3 print statement. It prints color coded, tagged messages that can be useful in debugging, or if you just prefer a cleaner appearance in your terminal. Please refer to the GitHub repo for more information'
version = '1.1.0'
url='https://github.com/MichaelDylan77/PrintTags'
author='Michael Lockyer'
author_email='mdlockyer@gmail.com'
license='MIT License'
classifiers = (
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
packages = find_packages()
    
setup(name=name, description=description, long_description=long_description, version=version, url=url, author=author, author_email=author_email, license=license, classifiers=classifiers, packages=packages)