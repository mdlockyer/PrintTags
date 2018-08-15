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

The current set of tags are:

* Info
* Success
* Notice
* Timeout
* Warn
* Error

There is also a test script included in this repo that will print a sample for each tag.
Just run `python3 test.py` from the repository root

## License

[View license file](./LICENSE)