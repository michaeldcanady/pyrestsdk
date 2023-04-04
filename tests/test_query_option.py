"""
Tests Query Options
===================
"""

from pyrestsdk.type.model import QueryOption

def test_query_option_init():
    """
    Tests Initializing a query option
    """

    query_option = QueryOption("page", 1)
    assert query_option.name == "page"
    assert query_option.value == 1
    assert str(query_option) == "page=1"

def test_query_option_equality():
    """
    Tests query options' ability to determine equity
    """

    query_option_1 = QueryOption("page", 1)
    query_option_2 = QueryOption("page", 1)
    assert query_option_1 == query_option_2

def test_query_option_inequality():
    """
    Tests query options' ability to determine inequity
    """

    query_option_1 = QueryOption("page", 1)
    query_option_2 = QueryOption("page", 2)
    assert query_option_1 != query_option_2

def test_query_option_str():
    """
    Tests if query option stringify's properly
    """

    query_option = QueryOption("page", 1)
    assert str(query_option) == "page=1"
