# -*- coding: utf-8 -*-

from ..PrintTags import Colors


# Pytest
def test_black_colorized_string():
    assert Colors.black('Black') == '\033[0;30mBlack\033[0m'


# Pytest
def test_red_colorized_string():
    assert Colors.red('Red') == '\033[0;31mRed\033[0m'


# Pytest
def test_green_colorized_string():
    assert Colors.green('Green') == '\033[0;32mGreen\033[0m'


# Pytest
def test_yellow_colorized_string():
    assert Colors.yellow('Yellow') == '\033[0;33mYellow\033[0m'


# Pytest
def test_blue_colorized_string():
    assert Colors.blue('Blue') == '\033[0;34mBlue\033[0m'


# Pytest
def test_magenta_colorized_string():
    assert Colors.magenta('Magenta') == '\033[0;35mMagenta\033[0m'


# Pytest
def test_cyan_colorized_string():
    assert Colors.cyan('Cyan') == '\033[0;36mCyan\033[0m'


# Pytest
def test_white_colorized_string():
    assert Colors.white('White') == '\033[0;37mWhite\033[0m'
