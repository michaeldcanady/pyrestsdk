"""Generic Tests
"""

from pyrestsdk.request import Request


def test_generic_type():
    """
    Test that generic gets the proper type
    """

    class ExampleRequest(Request[str]):
        """Example Class Type
        """
        pass

    _request = ExampleRequest("test.com", None, None)
    assert _request.generic_type is str
