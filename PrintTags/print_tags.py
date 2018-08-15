from os import getenv

# Print tags
info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '

# ANSII color codes
black_code: int = 30
red_code: int = 31
green_code: int = 32
yellow_code: int = 33
blue_code: int = 34
magenta_code: int = 35
cyan_code: int = 36
white_code: int = 37

# ANSII string format
base_string: str = '\033[0;{}m{}\033[0m'

def colorize(message, color=30):
    if getenv('ANSI_COLORS_DISABLED') is None:
        message = base_string.format(color, message)
    return message


# Basic color printouts

def black(message):
    print(colorize(message, color=black_code))

def red(message):
    print(colorize(message, color=red_code))

def green(message):
    print(colorize(message, color=green_code))

def yellow(message):
    print(colorize(message, color=yellow_code))

def blue(message):
    print(colorize(message, color=blue_code))

def magenta(message):
    print(colorize(message, color=magenta_code))

def cyan(message):
    print(colorize(message, color=cyan_code))

def white(message):
    print(colorize(message, color=white_code))

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