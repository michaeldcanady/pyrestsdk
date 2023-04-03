"""
PyTests for BaseRequest
=======================
"""

from unittest.mock import MagicMock

import pytest

from pyrestsdk.request import BaseRequest
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import (
    HeaderOptionCollection,
    QueryOptionCollection,
    QueryOption,
    HeaderOption,
)


class MockClient: #pylint: disable=[too-few-public-methods, too-many-ancestors]
    """
    Mock Client for testing
    """

    def __init__(self):
        self.get = MagicMock()
        self.post = MagicMock()
        self.delete = MagicMock()
        self.put = MagicMock()


class MockRequest(BaseRequest[str]): #pylint: disable=too-many-ancestors
    """
    Mock Request for testing
    """

    def parse_exception(self, *args):
        pass

    def send_request(self, *args):
        pass

    def parse_response(self, *args):
        pass


@pytest.fixture()
def mock_client() -> MockClient:
    """Gets the mock client Fixture

    Returns:
        MockClient: The mock client Fixture
    """

    return MockClient()


@pytest.fixture()
def base_request(
    mock_client: MockClient,  # pylint: disable=redefined-outer-name
) -> MockRequest:
    """Gets the base request fixture

    Args:
        mock_client (MockClient): The Test client

    Returns:
        MockRequest: The base request fixture
    """

    return MockRequest("https://example.com", mock_client, None)


def test_base_request_init(
    base_request: MockRequest,  # pylint: disable=redefined-outer-name
):
    """Resting intializing Request

    Args:
        base_request (MockRequest): The test request
    """

    assert base_request.request_url == "https://example.com"
    assert isinstance(base_request.header_options, HeaderOptionCollection)
    assert isinstance(base_request.query_options, QueryOptionCollection)


def test_base_request_parse_options(
    base_request: MockRequest,  # pylint: disable=redefined-outer-name
):
    """Tests parse options

    Args:
        base_request (MockRequest): The test request
    """

    base_request._parse_options(  # pylint: disable=protected-access
        [
            HeaderOption("Authorization", "Bearer TOKEN"),
            QueryOption("page", 1),
        ]
    )
    assert len(base_request.header_options) == 1
    assert base_request.header_options[0].name == "Authorization"
    assert base_request.header_options[0].value == "Bearer TOKEN"

    assert len(base_request.query_options) == 1
    assert base_request.query_options[0].name == "page"
    assert base_request.query_options[0].value == 1


def test_base_request_send_request( # pylint: disable=redefined-outer-name
    mock_client: MockClient,
    base_request: MockRequest,
):
    """Tests Sending Requests

    Args:
        mock_client (MockClient): The test client
        base_request (MockRequest): The test request
    """

    mock_client.get.reset_mock()
    mock_client.post.reset_mock()
    mock_client.delete.reset_mock()
    mock_client.put.reset_mock()

    base_request.request_method = HttpsMethod.GET
    base_request._send_request({}, None)  # pylint: disable=protected-access
    mock_client.get.assert_called_once()

    base_request.request_method = HttpsMethod.POST
    base_request._send_request({}, None)  # pylint: disable=protected-access
    mock_client.post.assert_called_once()

    base_request.request_method = HttpsMethod.DELETE
    base_request._send_request({}, None)  # pylint: disable=protected-access
    mock_client.delete.assert_called_once()

    base_request.request_method = HttpsMethod.PUT
    base_request._send_request({}, None)  # pylint: disable=protected-access
    mock_client.put.assert_called_once()


def test_base_request_send_request_invalid_method(
    base_request: MockRequest,  # pylint: disable=redefined-outer-name
):
    """Tests Base Request to Send Request with Invalid Method

    Args:
        base_request (MockRequest): The base request
    """

    base_request.request_method = HttpsMethod.PATCH
    with pytest.raises(TypeError):
        base_request._send_request({}, None)  # pylint: disable=protected-access
