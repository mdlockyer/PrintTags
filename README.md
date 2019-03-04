
<p align="center">
 <img width="650" height="150" src="https://raw.githubusercontent.com/MichaelDylan77/PrintTags/master/logo_large.png">
</p>

<p align="center">
  <a href="https://travis-ci.com/MichaelDylan77/PrintTags"><img src="https://travis-ci.com/MichaelDylan77/PrintTags.svg?branch=master"></a>
  <a href="https://pypi.org/project/PrintTags/"><img src="https://img.shields.io/pypi/v/PrintTags.svg"></a>
  <a href="https://github.com/MichaelDylan77/PrintTags/issues"><img src="https://img.shields.io/github/issues/michaeldylan77/PrintTags.svg"></a>
  <a href="https://coveralls.io/github/MichaelDylan77/PrintTags?branch=master"><img src="https://coveralls.io/repos/github/MichaelDylan77/PrintTags/badge.svg?branch=master"></a>
  <a href="https://github.com/MichaelDylan77/PrintTags/blob/master/LICENSE.md"><img src="https://img.shields.io/apm/l/vim-mode.svg"></a>
</p>

**PrintTags is a lightweight package designed to act as an alternative to the built-in Python 3 
print function. It prints color coded, tagged messages that can be useful in debugging, or if you 
just prefer a cleaner appearance in your terminal.**



#### Usage:

First, install PrintTags using pip:
```terminal
$ pip install PrintTags
```

Then simply import it, and call the desired print function:
```python
import PrintTags as pt

pt.info('My message')
```
Alternatively, import with a wildcard for direct access to the PrintTags methods:
```python
from PrintTags import *

info('My message')
```

Print Tags supports printing colors, or tagged colored messages. 

The tag methods include an argument for turning off tags, which will 
simply print the message in the color associated with that tag:
```python
# Will print "My message" in the success color
pt.success('My message', tag=False)
```
There are also color methods that will print a colored message directly:
```python
pt.green('My message')
```

The current set of tags are:

* info
* success
* notice
* timeout
* warn
* error

Included color methods are:

* black
* red
* green
* yellow
* blue
* magenta
* cyan
* white

All methods listed above will colorize the input string and print it to the console. If you need only to colorize a string without printing it, just import the `Colors` module and call the appropriate color method:

```python
from PrintTags import Colors

# Will return "My message" wrapped in the associated ANSI escape code
blue_message = Colors.blue('My message')
```

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