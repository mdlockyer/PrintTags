from termcolor import colored

info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '


def info(message):
    """
    Used for printing basic information.

    Color:
        Cyan
    Args:
        message: The message to be printed
    """
    print(colored('{}{}'.format(info_tag, message), 'cyan'))


def success(message):
    """
    Used to indicate the successful execution of a process.

    Color:
        Green
    Args:
        message: The message to be printed
    """
    print(colored('{}{}'.format(success_tag, message), 'green'))


def notice(message):
    """
    Used as means of printing important information.

    Color:
        Blue
    Args:
        message: The message to be printed
    """
    print(colored('{}{}'.format(notice_tag, message), 'blue'))


def timeout(message):
    """
    Used to indicate the timeout of a process.

    Color:
        Cyan
    Args:
        message: The message to be printed
    """
    print(colored('{}{}'.format(timeout_tag, message), 'yellow'))


def warn(message):
    """
    Used to highlight that there may be an issue, or that a process has failed.

    Color:
        Magenta
    Args:
        message: The message to be printed
    """
    print(colored('{}{}'.format(warn_tag, message), 'magenta'))


def error(message):
    """
    Can be used to print the description or message associated with an exception.

    Color:
        Red
    Args:
        message: The message to be printed
    """
    print(colored('{}{}'.format(error_tag, message), 'red'))


if __name__ == "__main__":
    pass