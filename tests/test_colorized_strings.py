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


"""

    print('\n')
    print(Colors.yellow('----------------------------------'))
    print(Colors.yellow('         Colorized strings'))
    print(Colors.yellow('----------------------------------'))
    print('\n')

    print(Colors.black('Black'))
    print(Colors.red('Red'))
    print(Colors.green('Green'))
    print(Colors.yellow('Yellow'))
    print(Colors.blue('Blue'))
    print(Colors.magenta('Magenta'))
    print(Colors.cyan('Cyan'))
    print(Colors.white('White'))

    

    print('\n')
    Colors.cyan('----------------------------------')
    Colors.cyan('          Colored printouts')
    Colors.cyan('----------------------------------')
    print('\n')
    
    black('Black')
    red('Red')
    green('Green')
    yellow('Yellow')
    blue('Blue')
    magenta('Magenta')
    cyan('Cyan')
    white('White')
    
    print('\n')
    green('----------------------------------')
    green('             Tag off')
    green('----------------------------------')
    print('\n')
    
    info('Info', tag=False)
    success('Success', tag=False)
    notice('Notice', tag=False)
    timeout('Timeout', tag=False)
    warn('Warn', tag=False)
    error('Error', tag=False)
    
    print('\n')
    blue('----------------------------------')
    blue('             Tags on')
    blue('----------------------------------')
    print('\n')
    
    info('Info')
    success('Success')
    notice('Notice')
    timeout('Timeout')
    warn('Warn')
    error('Error')
    
    print('\n')
    red('----------------------------------')
    red('             Arguments')
    red('----------------------------------')
    print('\n')
    
    info('I', 'n', 'f', 'o', sep='.', end='.\n')
    success('S', 'u', 'c', 'c', 'e', 's', 's', sep='.', end='.\n')
    notice('N', 'o', 't', 'i', 'c', 'e', sep='.', end='.\n')
    timeout('T', 'i', 'm', 'e', 'o', 'u', 't', sep='.', end='.\n')
    warn('W', 'a', 'r', 'n', sep='.', end='.\n')
    error('E', 'r', 'r', 'o', 'r', sep='.', end='.\n')
    
    print('\n')
    
    # Should not print or raise exception
    stdout.close()
    info('Info', tag=False, closed_ok=True)
    success('Success', tag=False, closed_ok=True)
    notice('Notice', tag=False, closed_ok=True)
    timeout('Timeout', tag=False, closed_ok=True)
    warn('Warn', tag=False, closed_ok=True)
    error('Error', tag=False, closed_ok=True)
    """
