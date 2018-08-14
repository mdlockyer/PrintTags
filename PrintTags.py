from termcolor import colored

# These are the standard console print tags

info_tag: str = '[info] '
success_tag: str = '[success] '
notice_tag: str = '[notice] '
timeout_tag: str = '[timeout] '
warn_tag: str = '[warn] '
exit_tag: str = '[exit] '
error_tag: str = '[error] '


def info(x):
    print(colored(f'{info_tag}{x}', 'cyan'))


def success(x):
    print(colored(f'{success_tag}{x}', 'green'))


def notice(x):
    print(colored(f'{notice_tag}{x}', 'yellow'))


def timeout(x):
    print(colored(f'{timeout_tag}{x}', 'grey'))


def warn(x):
    print(colored(f'{warn_tag}{x}', 'red'))


def exit(x):
    print(colored(f'{exit_tag}{x}', 'red'))


def error(x):
    print(colored(f'{error_tag}{x}', 'red'))


if __name__ == "__main__":
    pass