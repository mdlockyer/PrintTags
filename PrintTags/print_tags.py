# -*- coding: utf-8 -*-

from .colors import Colors

# Tags
info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '


def black(*args, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
    """
    Prints values in black

    Args:
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
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

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
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

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
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

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
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

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
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

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
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

    Args:
        tag (bool, optional): Whether or not the tag should be printed in front of the message
        closed_ok (bool, optional): Whether or not to catch the ValueError raised by a closed stdout
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = (error_tag, ) + args if tag else args
    red(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


if __name__ == "__main__":
    pass
