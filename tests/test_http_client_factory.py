from pyrestsdk.clientfactory import HTTPClientFactory
from pyrestsdk.middleware import BaseAuthorizationHandler
from requests import Session

def test_client_factory_with_custom_middleware():
    """
    Test that requests from a native HTTP client have a context object attached
    """
    
    middleware = [
        BaseAuthorizationHandler(None)
    ]
    
    client = HTTPClientFactory(Session()).create_with_custom_middleware(middleware)
    
    response = client.get("https://www.google.com")
    
    assert response.status_code == 200