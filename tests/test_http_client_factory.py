"""
HTTP Client Factory Tests
=========================
"""

from unittest.mock import MagicMock

from requests import Session

import pytest

from pyrestsdk.clientfactory import HTTPClientFactory
from pyrestsdk.credential import AbstractBasicCredential
from pyrestsdk.middleware import BaseMiddleware, MiddlewarePipeline

class MockBasicCredential(AbstractBasicCredential):
    """
    Mock Basic Credential for tesing
    """

class MockMiddleware(BaseMiddleware):
    """
    Mock Middleware for testing
    """

def test_http_client_factory_init():
    """
    Tests HTTP Client Factory init
    """

    session = MagicMock(spec=Session)
    factory = HTTPClientFactory("example.com", session, "https")
    assert factory._base_url == "example.com" #pylint: disable=protected-access
    assert factory._protocol == "https" #pylint: disable=protected-access
    assert factory.session == session

def test_http_client_factory_create_with_custom_middleware():
    """
    Tests create_with_custom_middleware method
    """

    session = Session()
    protocol = "https"
    factory = HTTPClientFactory("example.com", session, protocol)
    middleware = [MockMiddleware()]
    with pytest.raises(ValueError):
        factory.create_with_custom_middleware([])

    factory.create_with_custom_middleware(middleware)

    assert isinstance(factory.session.adapters[f"{protocol}://"], MiddlewarePipeline)

def test_http_client_factory_set_base_url():
    """
    Tests internal _set_base_url method
    """

    session = MagicMock(spec=Session)
    factory = HTTPClientFactory("example.com", session, "https")

    factory._set_base_url("api") #pylint: disable=protected-access

    assert session.base_url == "https://api.example.com"
