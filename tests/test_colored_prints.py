from ..PrintTags import black, red, green, yellow, blue, magenta, cyan, white
from io import StringIO
from contextlib import redirect_stdout

black_expected_value = '\x1b[0;30marg 1\x1b[0m\x1b[0;30m \x1b[0m\x1b[0;30marg 2\x1b[0m\x1b[0;30m\n\x1b[0m'
red_expected_value = '\x1b[0;31marg 1\x1b[0m\x1b[0;31m \x1b[0m\x1b[0;31marg 2\x1b[0m\x1b[0;31m\n\x1b[0m'
green_expected_value = '\x1b[0;32marg 1\x1b[0m\x1b[0;32m \x1b[0m\x1b[0;32marg 2\x1b[0m\x1b[0;32m\n\x1b[0m'
yellow_expected_value = '\x1b[0;33marg 1\x1b[0m\x1b[0;33m \x1b[0m\x1b[0;33marg 2\x1b[0m\x1b[0;33m\n\x1b[0m'
blue_expected_value = '\x1b[0;34marg 1\x1b[0m\x1b[0;34m \x1b[0m\x1b[0;34marg 2\x1b[0m\x1b[0;34m\n\x1b[0m'
magenta_expected_value = '\x1b[0;35marg 1\x1b[0m\x1b[0;35m \x1b[0m\x1b[0;35marg 2\x1b[0m\x1b[0;35m\n\x1b[0m'
cyan_expected_value = '\x1b[0;36marg 1\x1b[0m\x1b[0;36m \x1b[0m\x1b[0;36marg 2\x1b[0m\x1b[0;36m\n\x1b[0m'
white_expected_value = '\x1b[0;37marg 1\x1b[0m\x1b[0;37m \x1b[0m\x1b[0;37marg 2\x1b[0m\x1b[0;37m\n\x1b[0m'


def test_black():
    with StringIO() as buf, redirect_stdout(buf):
        black('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == black_expected_value


def test_red():
    with StringIO() as buf, redirect_stdout(buf):
        red('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == red_expected_value


def test_green():
    with StringIO() as buf, redirect_stdout(buf):
        green('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == green_expected_value


def test_yellow():
    with StringIO() as buf, redirect_stdout(buf):
        yellow('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == yellow_expected_value


def test_blue():
    with StringIO() as buf, redirect_stdout(buf):
        blue('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == blue_expected_value


def test_magenta():
    with StringIO() as buf, redirect_stdout(buf):
        magenta('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == magenta_expected_value


def test_cyan():
    with StringIO() as buf, redirect_stdout(buf):
        cyan('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == cyan_expected_value


def test_white():
    with StringIO() as buf, redirect_stdout(buf):
        white('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == white_expected_value
