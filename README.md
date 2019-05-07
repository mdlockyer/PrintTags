
<p align="center">
 <img width="650" src="https://raw.githubusercontent.com/MichaelDylan77/PrintTags/master/logo_large.png">
</p>

<p align="center">
  <a href="https://travis-ci.com/MichaelDylan77/PrintTags"><img src="https://travis-ci.com/MichaelDylan77/PrintTags.svg?branch=master" alt="Build Status"></a>
  <a href="https://printtags.readthedocs.io/en/latest/?badge=latest"><img src="https://readthedocs.org/projects/printtags/badge/?version=latest" alt="Documentation Status" /></a>
  <a href="https://pypi.org/project/PrintTags/"><img src="https://img.shields.io/pypi/v/PrintTags.svg" alt="Pypi Version"></a>
  <a href="https://github.com/MichaelDylan77/PrintTags/issues"><img src="https://img.shields.io/github/issues/michaeldylan77/PrintTags.svg" alt="Issues Status"></a>
  <a href="https://coveralls.io/github/MichaelDylan77/PrintTags?branch=master"><img src="https://coveralls.io/repos/github/MichaelDylan77/PrintTags/badge.svg?branch=master" alt="Code Coverage"></a>
  <a href="https://github.com/MichaelDylan77/PrintTags/blob/master/LICENSE.md"><img src="https://img.shields.io/apm/l/vim-mode.svg" alt="License"></a>
</p>

**PrintTags is a lightweight package designed to act as an alternative to the built-in Python 3 
print function. It prints color coded, tagged messages that can be useful in debugging, or if you 
just prefer a cleaner appearance in your terminal.**



#### Basic Usage:

First, install PrintTags using pip:
```shell
$ pip install PrintTags
```

Then simply import it, and call the desired print function:
```python
import PrintTags as pt

pt.info('My message')
```

There are also color methods that will print a colored message directly:
```python
pt.green('My message')
```

#### Arguments:

PrintTags is designed to be backward compatible with Python's default `print` function.
This means all functions within the PrintTags namespace accept the same keyword arguments as `print`:
```python
pt.success('positional', 'arguments', sep=' ', end='\n', file=None, flush=True)
```

These functions also include additional keyword arguments that are used to customize the output:

```python
# Prints using a user defined tag
pt.success('positional', 'arguments', tag='[custom_success]')
# Prepends a datetime stamp to the output
pt.success('positional', 'arguments', add_datetime=True)
# Prepends a prefix value to the output. This will not be 
# treated as a positional argument and therefore will not be
# separated by "sep" argument.
pt.success('positional', 'arguments', prefix='some_prefix')
pt.success('positional', 'arguments', prefix='some_prefix')
```

#### Colors:

All methods listed above will colorize the input string and print it to the console. If you need only to colorize a string without printing it, just import the `Colors` module and call the appropriate color method:

```python
from PrintTags import Colors

# Will return "My message" wrapped in the associated ANSI escape code
blue_message = Colors.blue('My message')
```

___

**PrintTags is designed to be fast, transparent, and simple. Its mission is
to extend Python's `print` function and have the smallest learning curve possible. 
To this end, it does not aspire to be a full-featured logging library. For users who require a more
in-depth logger, perhaps Python's built-in `logging` might be of interest.
There are also a number of open-source alternatives that are quite exceptional, namely
[Loguru](https://github.com/Delgan/loguru/blob/master/README.rst).**

### For a full API reference, [read the docs](https://printtags.readthedocs.io)

##### Example Output:

![](https://raw.githubusercontent.com/MichaelDylan77/PrintTags/master/example.png)


##### License:

[View license file](LICENSE.md)