# -*- coding: utf-8 -*-

# noinspection PyProtectedMember
from ..PrintTags.print_tags import _get_datetime, _print_with_color
# noinspection PyProtectedMember
from ..PrintTags.colors import _ANSIColor, Colors

from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime
import pytest
from os import remove

from typing import Tuple, Callable

color_fn_map: Tuple[Tuple[_ANSIColor, Callable[[str], str]], ...] = (
    (_ANSIColor.COLOR_BLACK, Colors.black),
    (_ANSIColor.COLOR_RED, Colors.red),
    (_ANSIColor.COLOR_GREEN, Colors.green),
    (_ANSIColor.COLOR_YELLOW, Colors.yellow),
    (_ANSIColor.COLOR_BLUE, Colors.blue),
    (_ANSIColor.COLOR_MAGENTA, Colors.magenta),
    (_ANSIColor.COLOR_CYAN, Colors.cyan),
    (_ANSIColor.COLOR_WHITE, Colors.white),
)


def test_get_timestamp() -> None:
    assert _get_datetime() == datetime.now().strftime('%d-%b-%Y %I:%M:%S%p')


@pytest.fixture
def reopen_stdout() -> None:
    yield
    remove('./mock_stdout')


@pytest.mark.usefixtures('reopen_stdout')
def test_print_with_color() -> None:
    arg_1: str = 'arg 1'
    arg_2: str = 'arg 2'
    prefix: str = 'prefix'
    sep: str = '-'
    end: str = '\n'
    for color, fn in color_fn_map:
        color_code: str = color.value
        with StringIO() as buf, redirect_stdout(buf):
            _print_with_color((arg_1, arg_2), fn, True, (prefix,), sep, end, False, None, False)
            actual_value = buf.getvalue()
            answer = (
                f'\033[0;{color_code}m{_get_datetime()} {prefix} {arg_1}\033[0m'
                f'\033[0;{color_code}m{sep}\033[0m'
                f'\033[0;{color_code}m{arg_2}\033[0m'
                f'\033[0;{color_code}m{end}\033[0m'
            )
            assert actual_value == answer
    # Test behavior when stdout is closed using the PrintTags `closed_ok` argument.
    with open('./mock_stdout', 'w') as stream:
        stream.close()
        with pytest.raises(ValueError):
            _print_with_color((arg_1, arg_2), Colors.red, True, (prefix,), sep, end, False, stream, False)
        _print_with_color((arg_1, arg_2), Colors.red, True, (prefix,), sep, end, True, stream, False)