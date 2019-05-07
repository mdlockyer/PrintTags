Getting Started
===============

PrintTags is designed to act as a replacement for the built in Python 3 print statement. It prints color coded, tagged messages that can be useful in debugging, or if you just prefer a cleaner appearance in your terminal.

First, install PrintTags using pip:

.. code-block:: bash

   pip install PrintTags

Then simply import it, and call the desired print function:

.. code-block:: python

   import PrintTags as pt

   pt.info('My message')

There are also color methods that will print a colored message directly:

.. code-block:: python

    pt.green('My message')

.. role:: python(code)
   :language: python

PrintTags is designed to be backward compatible with Python's default :python:`print` function.
This means all functions within the PrintTags namespace accept the same keyword arguments as :python:`print`:

.. code-block:: python

    pt.success('positional', 'arguments', sep=' ', end='\n', file=None, flush=True)

These functions also include additional keyword arguments that are used to customize the output:

.. code-block:: python

    # Prints using a user defined tag
    pt.success('positional', 'arguments', tag='[custom_success]')
    # Prepends a datetime stamp to the output
    pt.success('positional', 'arguments', add_datetime=True)
    # Prepends a prefix value to the output. This will not be
    # treated as a positional argument and therefore will not be
    # separated by "sep" argument.
    pt.success('positional', 'arguments', prefix='some_prefix')
    pt.success('positional', 'arguments', prefix='some_prefix')

All methods listed above will colorize the input string and print it to the console. If you need only to colorize a string without printing it, just import the `Colors` module and call the appropriate color method:

.. code-block:: python

    from PrintTags import Colors

    # Will return "My message" wrapped in the associated ANSI escape code
    blue_message = Colors.blue('My message')

Continue to the API Documentation for more information.