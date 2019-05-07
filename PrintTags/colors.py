# -*- coding: utf-8 -*-

# Verify that using ANSI color is supported
from os import getenv
_color_supported = getenv('ANSI_COLORS_DISABLED') is None

# ANSI color codes
_black_color = 30
_red_color = 31
_green_color = 32
_yellow_color = 33
_blue_color = 34
_magenta_color = 35
_cyan_color = 36
_white_color = 37

# ANSI string format
_base_string = '\033[0;{}m{}\033[0m'


def _colorize_string(string, color=_black_color) -> str:
    if _color_supported:
        string = _base_string.format(color, string)
    return string


class Colors(object):

    """
    Contains all the base methods responsible for wrapping
    input strings in ANSI escape codes
    """

    @staticmethod
    def black(string) -> str:
        """
        Colorizes a string to black

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_black_color)

    @staticmethod
    def red(string) -> str:
        """
        Colorizes a string to red

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_red_color)

    @staticmethod
    def green(string) -> str:
        """
        Colorizes a string to green

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_green_color)

    @staticmethod
    def yellow(string) -> str:
        """
        Colorizes a string to yellow

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_yellow_color)

    @staticmethod
    def blue(string) -> str:
        """
        Colorizes a string to blue

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_blue_color)

    @staticmethod
    def magenta(string) -> str:
        """
        Colorizes a string to magenta

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_magenta_color)

    @staticmethod
    def cyan(string) -> str:
        """
        Colorizes a string to cyan

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_cyan_color)

    @staticmethod
    def white(string) -> str:
        """
        Colorizes a string to white

        Args:
            string (str): The string to colorize
        Returns:
            str: The colorized string
        """
        return _colorize_string(string, color=_white_color)


if __name__ == "__main__":
    pass
