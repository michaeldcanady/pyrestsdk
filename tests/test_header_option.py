"""
Tests for Header Options
========================
"""

from pyrestsdk.type.model import HeaderOption

def test_header_option_init():
    """
    Tests Initializing a Header Option
    """

    header_option = HeaderOption("Authorization", "Bearer TOKEN")
    assert header_option.name == "Authorization"
    assert header_option.value == "Bearer TOKEN"
    assert str(header_option) == "Authorization:Bearer TOKEN"

def test_header_option_equality():
    """
    Checks if Header Options support equitity as it should
    """

    header_option_1 = HeaderOption("Authorization", "Bearer TOKEN")
    header_option_2 = HeaderOption("Authorization", "Bearer TOKEN")
    assert header_option_1 == header_option_2

def test_header_option_inequality():
    """
    Tests if Header Options support inequitity as it should
    """

    header_option_1 = HeaderOption("Authorization", "Bearer TOKEN")
    header_option_2 = HeaderOption("Authorization", "Bearer OTHER_TOKEN")
    assert header_option_1 != header_option_2

def test_header_option_str():
    """
    Tests if Header Option stringifies as intended
    """

    header_option = HeaderOption("Authorization", "Bearer TOKEN")
    assert str(header_option) == "Authorization:Bearer TOKEN"
