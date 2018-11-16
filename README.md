# PrintTags

 This package is designed to act as a replacement for the built in Python 3 print statement. It prints color coded, tagged messages that can be useful in debugging, or if you just prefer a cleaner appearance in your terminal.

![](example.png)

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

All methods listed above will colorize the input string and print it to the console. If you need only to colorize a string without printing it, simply import the `Colors` module and call the appropriate color method:

```python
from PrintTags import Colors

# Will return "My message" wrapped in the associated ANSI color formatting
blue_message = Colors.blue('My message')
```

## License

[View license file](./LICENSE)