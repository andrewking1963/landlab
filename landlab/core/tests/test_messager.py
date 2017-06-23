#! /usr/bin/env python
from nose.tools import assert_equal, assert_raises

from landlab.core.utils import (format_message, error_message,
                                warning_message, assert_or_print)


LOREM_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Pharetra pharetra massa massa ultricies mi quis hendrerit.

Dictumst vestibulum rhoncus est pellentesque. Sed viverra tellus in hac habitasse platea dictumst vestibulum rhoncus.
"""

def test_empty_message():
    """Test formatting an empty string."""
    assert_equal(format_message(''), '')


def test_one_line():
    """Test a single line message."""
    assert_equal(format_message('lorem ipsum'), 'lorem ipsum')


def test_leading_whitespace():
    """Test a single line message."""
    assert_equal(format_message('   lorem ipsum'), 'lorem ipsum')


def test_one_long_line():
    """Test a line that needs to be wrapped."""
    msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    assert_equal(format_message(msg),
                 """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua.""".strip())

def test_multiline():
    msg = """lorem
ipsum
    """
    assert_equal(format_message(msg), 'lorem ipsum')


def test_multiple_paragraphs():
    assert_equal(format_message(LOREM_IPSUM), """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua.

Pharetra pharetra massa massa ultricies mi quis hendrerit.

Dictumst vestibulum rhoncus est pellentesque. Sed viverra tellus in
hac habitasse platea dictumst vestibulum rhoncus.
""".strip())


def test_warning_message():
    msg = "Pharetra pharetra massa massa ultricies mi quis hendrerit."

    assert_equal(warning_message(msg),"""
WARNING
=======

Pharetra pharetra massa massa ultricies mi quis hendrerit.
                """.strip())


def test_error_message():
    msg = "Pharetra pharetra massa massa ultricies mi quis hendrerit."

    assert_equal(error_message(msg),"""
ERROR
=====

Pharetra pharetra massa massa ultricies mi quis hendrerit.
                """.strip())


def test_warning_message_is_none():
    assert_equal(warning_message(),"WARNING\n=======")


def test_error_message_is_none():
    assert_equal(error_message(),"ERROR\n=====")


def test_assert_or_pass():
    assert_or_print(True, onerror='pass')
    assert_or_print(False, onerror='pass')


def test_assert_or_warn():
    assert_or_print(True, onerror='warn')
    assert_or_print(False, onerror='warn')


def test_assert_or_raise():
    assert_or_print(True, onerror='raise')
    with assert_raises(AssertionError):
        assert_or_print(False, onerror='raise')
