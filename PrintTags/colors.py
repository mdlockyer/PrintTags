# -*- coding: utf-8 -*-

from os import getenv
from enum import Enum

# Verify that using ANSI color is supported
_color_is_supported: bool = getenv('ANSI_COLORS_DISABLED') is None


class _ANSIColor(Enum):
    COLOR_BLACK = 30
    COLOR_RED = 31
    COLOR_GREEN = 32
    COLOR_YELLOW = 33
    COLOR_BLUE = 34
    COLOR_MAGENTA = 35
    COLOR_CYAN = 36
    COLOR_WHITE = 37


def _colorize_string(value: str, color: _ANSIColor) -> str:
    if _color_is_supported:
        value = f'\033[0;{color.value}m{value}\033[0m'
    return value


class Colors(object):

    """
    Contains all the base methods responsible for wrapping
    input strings in ANSI escape codes
    """

    @staticmethod
    def black(value: str) -> str:
        """
        Colorizes a string to black

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_BLACK)

    @staticmethod
    def red(value: str) -> str:
        """
        Colorizes a string to red

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_RED)

    @staticmethod
    def green(value: str) -> str:
        """
        Colorizes a string to green

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_GREEN)

    @staticmethod
    def yellow(value: str) -> str:
        """
        Colorizes a string to yellow

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_YELLOW)

    @staticmethod
    def blue(value: str) -> str:
        """
        Colorizes a string to blue

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_BLUE)

    @staticmethod
    def magenta(value: str) -> str:
        """
        Colorizes a string to magenta

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_MAGENTA)

    @staticmethod
    def cyan(value: str) -> str:
        """
        Colorizes a string to cyan

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_CYAN)

    @staticmethod
    def white(value: str) -> str:
        """
        Colorizes a string to white

        Args:
            value (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(value, color=_ANSIColor.COLOR_WHITE)


if __name__ == "__main__":
    pass
