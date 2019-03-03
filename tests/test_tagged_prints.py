from ..PrintTags import info, success, notice, timeout, warn, error
from io import StringIO
from contextlib import redirect_stdout

info_expected_value = '\x1b[0;36m[info] arg 1\x1b[0m\x1b[0;36m \x1b[0m\x1b[0;36marg 2\x1b[0m\x1b[0;36m\n\x1b[0m'
success_expected_value = '\x1b[0;32m[success] arg 1\x1b[0m\x1b[0;32m \x1b[0m\x1b[0;32marg 2\x1b[0m\x1b[0;32m\n\x1b[0m'
notice_expected_value = '\x1b[0;34m[notice] arg 1\x1b[0m\x1b[0;34m \x1b[0m\x1b[0;34marg 2\x1b[0m\x1b[0;34m\n\x1b[0m'
timeout_expected_value = '\x1b[0;33m[timeout] arg 1\x1b[0m\x1b[0;33m \x1b[0m\x1b[0;33marg 2\x1b[0m\x1b[0;33m\n\x1b[0m'
warn_expected_value = '\x1b[0;35m[warn] arg 1\x1b[0m\x1b[0;35m \x1b[0m\x1b[0;35marg 2\x1b[0m\x1b[0;35m\n\x1b[0m'
error_expected_value = '\x1b[0;31m[error] arg 1\x1b[0m\x1b[0;31m \x1b[0m\x1b[0;31marg 2\x1b[0m\x1b[0;31m\n\x1b[0m'


def test_info():
    with StringIO() as buf, redirect_stdout(buf):
        info('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == info_expected_value


def test_success():
    with StringIO() as buf, redirect_stdout(buf):
        success('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == success_expected_value


def test_notice():
    with StringIO() as buf, redirect_stdout(buf):
        notice('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == notice_expected_value


def test_timeout():
    with StringIO() as buf, redirect_stdout(buf):
        timeout('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == timeout_expected_value


def test_warn():
    with StringIO() as buf, redirect_stdout(buf):
        warn('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == warn_expected_value


def test_error():
    with StringIO() as buf, redirect_stdout(buf):
        error('arg 1', 'arg 2')
        actual_value = buf.getvalue()
        assert actual_value == error_expected_value
