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


def _insert_tag(tag, *args) -> list:
    tag = str(tag)
    if not tag.endswith(' '):
        tag += ' '
    # Make args mutable as a list
    args = list(args)
    # Attach tag to first arg so separator doesn't catch it
    args[0] = tag + str(args[0])
    return args


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
        print(*[Colors.black(arg) for arg in args],
              sep=Colors.black(sep),
              end=Colors.black(end),
              file=file,
              **kwargs)
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
        print(*[Colors.red(arg) for arg in args],
              sep=Colors.red(sep),
              end=Colors.red(end),
              file=file,
              **kwargs)
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
        print(*[Colors.green(arg) for arg in args],
              sep=Colors.green(sep),
              end=Colors.green(end),
              file=file,
              **kwargs)
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
        print(*[Colors.yellow(arg) for arg in args],
              sep=Colors.yellow(sep),
              end=Colors.yellow(end),
              file=file,
              **kwargs)
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
        print(*[Colors.blue(arg) for arg in args],
              sep=Colors.blue(sep),
              end=Colors.blue(end),
              file=file,
              **kwargs)
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
        print(*[Colors.magenta(arg) for arg in args],
              sep=Colors.magenta(sep),
              end=Colors.magenta(end),
              file=file,
              **kwargs)
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
        print(*[Colors.cyan(arg) for arg in args],
              sep=Colors.cyan(sep),
              end=Colors.cyan(end),
              file=file,
              **kwargs)
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
        print(*[Colors.white(arg) for arg in args],
              sep=Colors.white(sep),
              end=Colors.white(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


# Tagged color printouts


def info(*args, tag=info_tag, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
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

    args = args if tag is None else _insert_tag(tag, *args)
    cyan(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def success(*args, tag=success_tag, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
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

    args = args if tag is None else _insert_tag(tag, *args)
    green(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def notice(*args, tag=notice_tag, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
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

    args = args if tag is None else _insert_tag(tag, *args)
    blue(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def timeout(*args, tag=timeout_tag, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
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

    args = args if tag is None else _insert_tag(tag, *args)
    yellow(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def warn(*args, tag=warn_tag, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
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

    args = args if tag is None else _insert_tag(tag, *args)
    magenta(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def error(*args, tag=error_tag, closed_ok=False, sep=' ', end='\n', file=None, **kwargs):
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

    args = args if tag is None else _insert_tag(tag, *args)
    red(*args, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


if __name__ == "__main__":
    pass
