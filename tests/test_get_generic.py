from pyrestsdk.request import Request


def get_generic_type():
    
    class ExampleRequest(Request[str]):
        pass
    
    _request = ExampleRequest("test.com", None, None)
    assert _request._generic_type is str