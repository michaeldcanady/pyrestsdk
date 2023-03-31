"""Header tests
"""

from pyrestsdk.type.model import HeaderOption, HeaderOptionCollection

def test_headers():
    """Test that headers collection appears as Dict[str, str]
    """

    collection = HeaderOptionCollection()

    collection.append(HeaderOption(1, "test"))

    headers_dict = collection.as_dict

    assert isinstance(headers_dict, dict)
    assert isinstance(list(headers_dict.keys())[0], str)
    assert isinstance(list(headers_dict.values())[0], str)

def test_longer_headers():
    """Test that longer headers collection appears as Dict[str,str]
    """

    collection = HeaderOptionCollection()

    for i in range(10):
        collection.append(HeaderOption(i, "test"))

    headers_dict = collection.as_dict

    assert isinstance(headers_dict, dict)
    assert isinstance(list(headers_dict.keys())[0], str)
    assert isinstance(list(headers_dict.values())[0], str)
