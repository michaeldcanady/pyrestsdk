import pytest
from unittest.mock import MagicMock

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import HeaderOptionCollection, QueryOptionCollection, QueryOption, HeaderOption

class MockClient:
    def __init__(self):
        self.get = MagicMock()
        self.post = MagicMock()
        self.delete = MagicMock()
        self.put = MagicMock()
    
class MockRequest(BaseRequest[str]):

    def parse_exception(self, *args):
        pass

    def send_request(self, *args):
        pass

    def parse_response(self, *args):
        pass

@pytest.fixture()
def mock_client():
    return MockClient()

@pytest.fixture()
def base_request(mock_client):
    return MockRequest("https://example.com", mock_client, None)

def test_base_request_init(base_request):
    assert base_request.request_url == "https://example.com"
    assert isinstance(base_request.header_options, HeaderOptionCollection)
    assert isinstance(base_request.query_options, QueryOptionCollection)

def test_base_request_parse_options(base_request):
    base_request._parse_options([
        HeaderOption("Authorization", "Bearer TOKEN"),
        QueryOption("page", 1),
    ])
    assert len(base_request.header_options) == 1
    assert base_request.header_options[0].name == "Authorization"
    assert base_request.header_options[0].value == "Bearer TOKEN"

    assert len(base_request.query_options) == 1
    assert base_request.query_options[0].name == "page"
    assert base_request.query_options[0].value == 1

def test_base_request_send_request(mock_client, base_request):
    mock_client.get.reset_mock()
    mock_client.post.reset_mock()
    mock_client.delete.reset_mock()
    mock_client.put.reset_mock()

    base_request.request_method = HttpsMethod.GET
    base_request._send_request({}, None)
    mock_client.get.assert_called_once()

    base_request.request_method = HttpsMethod.POST
    base_request._send_request({}, None)
    mock_client.post.assert_called_once()

    base_request.request_method = HttpsMethod.DELETE
    base_request._send_request({}, None)
    mock_client.delete.assert_called_once()

    base_request.request_method = HttpsMethod.PUT
    base_request._send_request({}, None)
    mock_client.put.assert_called_once()

def test_base_request_send_request_invalid_method(base_request):
    base_request.request_method = HttpsMethod.PATCH
    with pytest.raises(TypeError):
        base_request._send_request({}, None)
