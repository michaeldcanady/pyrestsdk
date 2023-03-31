from unittest.mock import MagicMock

from requests import Session

import pytest

from pyrestsdk.clientfactory import HTTPClientFactory
from pyrestsdk.credential import AbstractBasicCredential
from pyrestsdk.middleware import BaseMiddleware, MiddlewarePipeline

class MockBasicCredential(AbstractBasicCredential):
    pass

class MockMiddleware(BaseMiddleware):
    pass

def test_http_client_factory_init():
    session = MagicMock(spec=Session)
    factory = HTTPClientFactory("example.com", session, "https")
    assert factory._base_url == "example.com"
    assert factory._protocol == "https"
    assert factory.session == session

def test_http_client_factory_create_with_custom_middleware():
    session = Session()
    protocol = "https"
    factory = HTTPClientFactory("example.com", session, protocol)
    middleware = [MockMiddleware()]
    with pytest.raises(ValueError):
        factory.create_with_custom_middleware([])

    factory.create_with_custom_middleware(middleware)

    assert isinstance(factory.session.adapters[f"{protocol}://"], MiddlewarePipeline)

def test_http_client_factory_set_base_url():
    session = MagicMock(spec=Session)
    factory = HTTPClientFactory("example.com", session, "https")

    factory._set_base_url("api")

    assert session.base_url == "https://api.example.com"
