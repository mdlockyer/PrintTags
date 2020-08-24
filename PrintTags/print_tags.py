# -*- coding: utf-8 -*-

from datetime import datetime

from .colors import Colors

from typing import List, Tuple, TextIO, Optional, Callable, Any


def _get_datetime() -> str:
    return datetime.now().strftime('%d-%b-%Y %I:%M:%S%p')


def _print_with_color(args: Tuple[Any, ...], color_fn: Callable[[str], str],
                      add_datetime: bool, prefixes: Tuple[Optional[str], ...],
                      sep: str, end: str, closed_ok: bool, file: Optional[TextIO],
                      flush: bool) -> None:
    _args: List[str] = [str(arg) for arg in args]
    for prefix in reversed(prefixes):
        if prefix is None:
            continue
        # Add a space to the end of the prefix if is doesn't already have one
        _args[0] = f'{prefix}{_args[0]}' if prefix.endswith(' ') else f'{prefix} {_args[0]}'
    if add_datetime:
        _args[0] = f'{_get_datetime()} {_args[0]}'
    _args = [color_fn(arg) for arg in _args]
    try:
        print(*_args, sep=color_fn(sep), end=color_fn(end), file=file, flush=flush)
    except ValueError:
        if closed_ok:
            pass
        else:
            raise


def black(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
          sep: str = ' ', end: str = '\n', closed_ok: bool = False,
          file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in black.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.black, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def red(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
        sep: str = ' ', end: str = '\n', closed_ok: bool = False,
        file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in red.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.red, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def green(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
          sep: str = ' ', end: str = '\n', closed_ok: bool = False,
          file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in green.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.green, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def yellow(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
           sep: str = ' ', end: str = '\n', closed_ok: bool = False,
           file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in yellow.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.yellow, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def blue(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
         sep: str = ' ', end: str = '\n', closed_ok: bool = False,
         file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in blue.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.blue, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def magenta(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
            sep: str = ' ', end: str = '\n', closed_ok: bool = False,
            file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in magenta.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.magenta, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def cyan(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
         sep: str = ' ', end: str = '\n', closed_ok: bool = False,
         file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in cyan.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.cyan, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


def white(*args: Any, add_datetime: bool = False, prefix: Optional[str] = None,
          sep: str = ' ', end: str = '\n', closed_ok: bool = False,
          file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Prints values in white.

    Args:
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (any, optional): A string interpolatable value that should be prepended to the print. Default `None`.
        sep (str, optional): String inserted between values, default is a space. Default `' '`.
        end (str, optional): String appended after the last value, default is a newline. Default `\n`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file: A file-like object (stream, optional): Defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): Whether to forcibly flush the stream. Default `False`.
    """

    _print_with_color(args, Colors.white, add_datetime, (prefix,), sep, end, closed_ok, file, flush)


# MARK: Tagged color printouts

def info(*args: Any, tag_text: Optional[str] = 'info', add_datetime: bool = False,
         prefix: Optional[str] = None, sep: str = ' ', end: str = '\n', closed_ok: bool = False,
         file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Used for printing basic information.

    Args:
        tag_text (str, optional): The text content of the tag that will be prepended to the print.
            `None` for no tag. Default `'info'`.
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (str, optional): A string interpolatable value that will be prepended to the print. Default `None`.
        sep (str, optional): string inserted between values, default is a space. Default `' '`.
        end (str, optional): string appended after the last value, default is a newline. Default `'\n'`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file (TextIO, optional): defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): whether to forcibly flush the stream. Default `False`.
    """

    tag: Optional[str] = tag_text if tag_text is None else f'[{tag_text}]'
    _print_with_color(args, Colors.cyan, add_datetime, (prefix, tag), sep, end, closed_ok, file, flush)


def success(*args: Any, tag_text: Optional[str] = 'success', add_datetime: bool = False,
            prefix: Optional[str] = None, sep: str = ' ', end: str = '\n', closed_ok: bool = False,
            file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Used to indicate successful execution.

    Args:
        tag_text (str, optional): The text content of the tag that will be prepended to the print.
            `None` for no tag. Default `'success'`.
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (str, optional): A string interpolatable value that will be prepended to the print. Default `None`.
        sep (str, optional): string inserted between values, default is a space. Default `' '`.
        end (str, optional): string appended after the last value, default is a newline. Default `'\n'`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file (TextIO, optional): defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): whether to forcibly flush the stream. Default `False`.
    """

    tag: Optional[str] = tag_text if tag_text is None else f'[{tag_text}]'
    _print_with_color(args, Colors.green, add_datetime, (prefix, tag), sep, end, closed_ok, file, flush)


def notice(*args: Any, tag_text: Optional[str] = 'notice', add_datetime: bool = False,
           prefix: Optional[str] = None, sep: str = ' ', end: str = '\n', closed_ok: bool = False,
           file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Used to print important information.

    Args:
        tag_text (str, optional): The text content of the tag that will be prepended to the print.
            `None` for no tag. Default `'notice'`.
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (str, optional): A string interpolatable value that will be prepended to the print. Default `None`.
        sep (str, optional): string inserted between values, default is a space. Default `' '`.
        end (str, optional): string appended after the last value, default is a newline. Default `'\n'`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file (TextIO, optional): defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): whether to forcibly flush the stream. Default `False`.
    """

    tag: Optional[str] = tag_text if tag_text is None else f'[{tag_text}]'
    _print_with_color(args, Colors.blue, add_datetime, (prefix, tag), sep, end, closed_ok, file, flush)


def timeout(*args: Any, tag_text: Optional[str] = 'timeout', add_datetime: bool = False,
            prefix: Optional[str] = None, sep: str = ' ', end: str = '\n', closed_ok: bool = False,
            file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Used to indicate a timeout.

    Args:
        tag_text (str, optional): The text content of the tag that will be prepended to the print.
            `None` for no tag. Default `'timeout'`.
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (str, optional): A string interpolatable value that will be prepended to the print. Default `None`.
        sep (str, optional): string inserted between values, default is a space. Default `' '`.
        end (str, optional): string appended after the last value, default is a newline. Default `'\n'`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file (TextIO, optional): defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): whether to forcibly flush the stream. Default `False`.
    """

    tag: Optional[str] = tag_text if tag_text is None else f'[{tag_text}]'
    _print_with_color(args, Colors.yellow, add_datetime, (prefix, tag), sep, end, closed_ok, file, flush)


def warn(*args: Any, tag_text: Optional[str] = 'warn', add_datetime: bool = False,
         prefix: Optional[str] = None, sep: str = ' ', end: str = '\n', closed_ok: bool = False,
         file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Used to highlight that there may be an issue, or that code has improperly executed.

    Args:
        tag_text (str, optional): The text content of the tag that will be prepended to the print.
            `None` for no tag. Default `'warn'`.
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (str, optional): A string interpolatable value that will be prepended to the print. Default `None`.
        sep (str, optional): string inserted between values, default is a space. Default `' '`.
        end (str, optional): string appended after the last value, default is a newline. Default `'\n'`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file (TextIO, optional): defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): whether to forcibly flush the stream. Default `False`.
    """

    tag: Optional[str] = tag_text if tag_text is None else f'[{tag_text}]'
    _print_with_color(args, Colors.magenta, add_datetime, (prefix, tag), sep, end, closed_ok, file, flush)


def error(*args: Any, tag_text: Optional[str] = 'error', add_datetime: bool = False,
          prefix: Optional[str] = None, sep: str = ' ', end: str = '\n', closed_ok: bool = False,
          file: Optional[TextIO] = None, flush: bool = False) -> None:
    """
    Can be used to print the description or message associated with an exception.

    Args:
        tag_text (str, optional): The text content of the tag that will be prepended to the print.
            `None` for no tag. Default `'error'`.
        add_datetime (bool, optional): Whether or not a datetime timestamp should be printed. Default `False`.
        prefix (str, optional): A string interpolatable value that will be prepended to the print. Default `None`.
        sep (str, optional): string inserted between values, default is a space. Default `' '`.
        end (str, optional): string appended after the last value, default is a newline. Default `'\n'`.
        closed_ok (bool, optional): Whether or not the ValueError raised by a closed stdout should be
            suppressed. Default `False`.
        file (TextIO, optional): defaults to the current sys.stdout. Default `None`.
        flush (bool, optional): whether to forcibly flush the stream. Default `False`.
    """

    tag: Optional[str] = tag_text if tag_text is None else f'[{tag_text}]'
    _print_with_color(args, Colors.red, add_datetime, (prefix, tag), sep, end, closed_ok, file, flush)


if __name__ == "__main__":
    pass
