from termcolor import colored

info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '


def info(x):
    print(colored('{}{}'.format(info_tag, x), 'cyan'))


def success(x):
    print(colored('{}{}'.format(success_tag, x), 'green'))


def notice(x):
    print(colored('{}{}'.format(notice_tag, x), 'blue'))


def timeout(x):
    print(colored('{}{}'.format(timeout_tag, x), 'yellow'))


def warn(x):
    print(colored('{}{}'.format(warn_tag, x), 'magenta'))


def error(x):
    print(colored('{}{}'.format(error_tag, x), 'red'))


if __name__ == "__main__":
    pass