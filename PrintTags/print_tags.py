# -*- coding: utf-8 -*-

from datetime import datetime

from .colors import Colors

# Tags
info_tag = '[info] '
success_tag = '[success] '
notice_tag = '[notice] '
timeout_tag = '[timeout] '
warn_tag = '[warn] '
exit_tag = '[exit] '
error_tag = '[error] '


def _insert_prefix(prefix, *args) -> list:
    prefix = str(prefix)
    # Make args mutable as a list
    args = list(args)
    if not prefix.endswith(' '):
        prefix += ' '
    # Attach tag to first arg so separator doesn't catch it
    args[0] = prefix + str(args[0])
    return args


def _get_timestamp() -> str:
    return datetime.now().strftime('%d-%b-%Y %I:%M:%S%p ')


def black(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in black

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.black(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.black(sep),
              end=Colors.black(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def red(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in red

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.red(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.red(sep),
              end=Colors.red(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def green(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in green

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.green(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.green(sep),
              end=Colors.green(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def yellow(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in yellow

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.yellow(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.yellow(sep),
              end=Colors.yellow(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def blue(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in blue

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.blue(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.blue(sep),
              end=Colors.blue(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def magenta(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in magenta

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.magenta(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.magenta(sep),
              end=Colors.magenta(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def cyan(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in cyan

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.cyan(arg) for arg in args]
    try:
        print(*args,
              sep=Colors.cyan(sep),
              end=Colors.cyan(end),
              file=file,
              **kwargs)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def white(*args, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Prints values in white

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(prefix, *args) if prefix else args
    args = _insert_prefix(_get_timestamp(), *args) if add_datetime else args
    args = [Colors.white(arg) for arg in args]
    try:
        print(*args,
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

def info(*args, tag=info_tag, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Used for printing basic information.

    Args:
        tag (any, optional): The tag that will be prepended to the print. None or False for no tag
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that will be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(tag, *args) if tag else args
    cyan(*args, add_datetime=add_datetime, prefix=prefix, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def success(*args, tag=success_tag, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Used to indicate the successful execution of a process.

    Args:
        tag (any, optional): The tag that will be prepended to the print. None or False for no tag
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(tag, *args) if tag else args
    green(*args, add_datetime=add_datetime, prefix=prefix, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def notice(*args, tag=notice_tag, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Used to print important information.

    Args:
        tag (any, optional): The tag that will be prepended to the print. None or False for no tag
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(tag, *args) if tag else args
    blue(*args, add_datetime=add_datetime, prefix=prefix, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def timeout(*args, tag=timeout_tag, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Used to indicate the timeout of a process.

    Args:
        tag (any, optional): The tag that will be prepended to the print. None or False for no tag
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(tag, *args) if tag else args
    yellow(*args, add_datetime=add_datetime, prefix=prefix, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def warn(*args, tag=warn_tag, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Used to highlight that there may be an issue, or that code has improperly executed.

    Args:
        tag (any, optional): The tag that will be prepended to the print. None or False for no tag
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(tag, *args) if tag else args
    magenta(*args, add_datetime=add_datetime, prefix=prefix, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


def error(*args, tag=error_tag, add_datetime=False, prefix=None, sep=' ', end='\n', closed_ok=False, file=None, **kwargs):
    """
    Can be used to print the description or message associated with an exception.

    Args:
        tag (any, optional): The tag that will be prepended to the print. None or False for no tag
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed
        prefix (any, optional): A string interpolatable value that should be prepended to the print
        sep (str, optional): string inserted between values, default is a space.
        end (str, optional): string appended after the last value, default is a newline.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be suppressed
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush (bool, optional): whether to forcibly flush the stream.
    """

    args = _insert_prefix(tag, *args) if tag else args
    red(*args, add_datetime=add_datetime, prefix=prefix, sep=sep, end=end, file=file, closed_ok=closed_ok, **kwargs)


if __name__ == "__main__":
    pass
