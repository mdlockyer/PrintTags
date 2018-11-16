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

def colorize(message, color=30):
    if getenv('ANSI_COLORS_DISABLED') is None:
        message = base_string.format(color, message)
    return message

# Basic color printouts

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
        return colorize(string, color=black_code)

    @staticmethod
    def red(string):
        """
        Colorizes a string to red

        Args:
            string: The string to colorize
        """
        return colorize(string, color=red_code)

    @staticmethod
    def green(string):
        """
        Colorizes a string to green

        Args:
            string: The string to colorize
        """
        return colorize(string, color=green_code)

    @staticmethod
    def yellow(string):
        """
        Colorizes a string to yellow

        Args:
            string: The string to colorize
        """
        return colorize(string, color=yellow_code)

    @staticmethod
    def blue(string):
        """
        Colorizes a string to blue

        Args:
            string: The string to colorize
        """
        return colorize(string, color=blue_code)

    @staticmethod
    def magenta(string):
        """
        Colorizes a string to magenta

        Args:
            string: The string to colorize
        """
        return colorize(string, color=magenta_code)

    @staticmethod
    def cyan(string):
        """
        Colorizes a string to cyan

        Args:
            string: The string to colorize
        """
        return colorize(string, color=cyan_code)

    @staticmethod
    def white(string):
        """
        Colorizes a string to white

        Args:
            string: The string to colorize
        """
        return colorize(string, color=white_code)



def black(message):
    """
    Prints a message in black

    Args:
        message: The message to print
    """
    print(Colors.black(message))

def red(message):
    """
    Prints a message in red

    Args:
        message: The message to print
    """
    print(Colors.red(message))

def green(message):
    """
    Prints a message in green

    Args:
        message: The message to print
    """
    print(Colors.green(message))

def yellow(message):
    """
    Prints a message in yellow

    Args:
        message: The message to print
    """
    print(Colors.yellow(message))

def blue(message):
    """
    Prints a message in blue

    Args:
        message: The message to print
    """
    print(Colors.blue(message))

def magenta(message):
    """
    Prints a message in magenta

    Args:
        message: The message to print
    """
    print(Colors.magenta(message))

def cyan(message):
    """
    Prints a message in cyan

    Args:
        message: The message to print
    """
    print(Colors.cyan(message))

def white(message):
    """
    Prints a message in white

    Args:
        message: The message to print
    """
    print(Colors.white(message))

# Tagged color printouts

def info(message, tag=True):
    """
    Used for printing basic information.

    Color:
        Cyan
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(info_tag, message) if tag else message
    cyan(message)


def success(message, tag=True):
    """
    Used to indicate the successful execution of a process.

    Color:
        Green
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(success_tag, message) if tag else message
    green(message)


def notice(message, tag=True):
    """
    Used as means of printing important information.

    Color:
        Blue
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(notice_tag, message) if tag else message
    blue(message)


def timeout(message, tag=True):
    """
    Used to indicate the timeout of a process.

    Color:
        Cyan
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(timeout_tag, message) if tag else message
    yellow(message)


def warn(message, tag=True):
    """
    Used to highlight that there may be an issue, or that a process has failed.

    Color:
        Magenta
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(warn_tag, message) if tag else message
    magenta(message)


def error(message, tag=True):
    """
    Can be used to print the description or message associated with an exception.

    Color:
        Red
    Args:
        message: The message to be printed
        tag: Whether or not the tag should be printed in front of the message
    """
    message = '{}{}'.format(error_tag, message) if tag else message
    red(message)

if __name__ == "__main__":
    pass