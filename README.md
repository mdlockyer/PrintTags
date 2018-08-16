# Print Tags

 This package is designed to act as a replacement for the built in Python 3 print statement. It prints color coded, tagged messages that can be useful in debugging, or if you just prefer a cleaner appearance in your terminal.

## Usage

First, install PrintTags using pip:
```
pip install PrintTags
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

There is also a test script included in this repo that will print a sample for each tag.
Just run `python3 test.py` from the repository root

## License

[View license file](./LICENSE)