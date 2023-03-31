from pyrestsdk.type.model import QueryOption

def test_query_option_init():
    query_option = QueryOption("page", 1)
    assert query_option.name == "page"
    assert query_option.value == 1
    assert str(query_option) == "page=1"

def test_query_option_equality():
    query_option_1 = QueryOption("page", 1)
    query_option_2 = QueryOption("page", 1)
    assert query_option_1 == query_option_2

def test_query_option_inequality():
    query_option_1 = QueryOption("page", 1)
    query_option_2 = QueryOption("page", 2)
    assert query_option_1 != query_option_2

def test_query_option_str():
    query_option = QueryOption("page", 1)
    assert str(query_option) == "page=1"