# -*- coding: utf-8 -*-

from os import getenv

# TODO: Correct colors

# Print tags
info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '

# ANSI color codes
black_code: int = 30
red_code: int = 31
green_code: int = 32
yellow_code: int = 33
blue_code: int = 34
magenta_code: int = 35
cyan_code: int = 36
white_code: int = 37

# ANSI string format
base_string: str = '\033[0;{}m{}\033[0m'


def colorize_string(message, color=30):
    if getenv('ANSI_COLORS_DISABLED') is None:
        message = base_string.format(color, message)
    return message


class Colors(object):

    """
    Contains all the base methods responsible for wrapping 
    input strings in the correct ANSI string formatting
    """

    @staticmethod
    def black(string):
        """
        Colorizes a string to black

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=black_code)

    @staticmethod
    def red(string):
        """
        Colorizes a string to red

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=red_code)

    @staticmethod
    def green(string):
        """
        Colorizes a string to green

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=green_code)

    @staticmethod
    def yellow(string):
        """
        Colorizes a string to yellow

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=yellow_code)

    @staticmethod
    def blue(string):
        """
        Colorizes a string to blue

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=blue_code)

    @staticmethod
    def magenta(string):
        """
        Colorizes a string to magenta

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=magenta_code)

    @staticmethod
    def cyan(string):
        """
        Colorizes a string to cyan

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=cyan_code)

    @staticmethod
    def white(string):
        """
        Colorizes a string to white

        Args:
            string: The string to colorize
        """
        return colorize_string(string, color=white_code)


def black(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in black

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.black(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def red(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in red

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.red(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def green(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in green

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.green(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def yellow(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in yellow

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.yellow(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def blue(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in blue

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.blue(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def magenta(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in magenta

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.magenta(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def cyan(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in cyan

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.cyan(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def white(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in white

    Args:
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        flush (bool, optional): whether to forcibly flush the stream.
    """
    try:
        args = [Colors.white(arg) for arg in args]
        print(*args, sep=sep, end=end, file=file, **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


# Tagged color printouts


def info(*args, tag=True, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Used for printing basic information.
    tag: [info]
    color: cyan

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (info_tag, ) + args if tag else args
    cyan(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def success(*args, tag=True, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Used to indicate the successful execution of a process.
    tag: [success]
    color: green

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (success_tag, ) + args if tag else args
    green(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def notice(*args, tag=True, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Used to print important information.
    tag: [notice]
    color: blue

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (notice_tag, ) + args if tag else args
    blue(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def timeout(*args, tag=True, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Used to indicate the timeout of a process.
    tag: [timeout]
    color: yellow

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (timeout_tag, ) + args if tag else args
    yellow(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def warn(*args, tag=True, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Used to highlight that there may be an issue, or that code has improperly executed.
    tag: [warn]
    color: magenta

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (warn_tag, ) + args if tag else args
    magenta(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def error(*args, tag=True, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Can be used to print the description or message associated with an exception.
    tag: [error]
    color: red

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional) Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (error_tag, ) + args if tag else args
    red(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


if __name__ == "__main__":
    pass
