"""
Request Builder Tests
=====================

"""

from typing import Optional, Union, List

from unittest.mock import MagicMock

import pytest

from pyrestsdk import ServiceClient
from pyrestsdk.requestbuilder._entity_request_builder import (
    EntityRequestBuilder as AbstractEntityRequestBuilder,
)
from pyrestsdk.request import BaseRequest
from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.request.supports_types._supports_base_invoke_request import (
    SupportsBaseInvokeRequest,
)
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import Entity


class MockServiceClient(ServiceClient):
    """
    Service Client for testing
    """

    def _get_session(self):  # pylint: disable=arguments-differ
        return self.session

    def _instance_url(self):  # pylint: disable=arguments-differ
        pass

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def patch(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def head(self, *args, **kwargs):
        pass

    def options(self, *args, **kwargs):
        pass

    @staticmethod
    def _initialize_session_and_base_url(*args, **kwargs):
        pass

    def get_resolved_url(self, url: str):
        pass


class MockBaseRequestBuilder(BaseRequestBuilder):
    """
    Test Base Request Builder
    """


class MockSupportsBaseInvokeRequest(SupportsBaseInvokeRequest[Entity]): #pylint: disable=too-many-ancestors
    """
    Test Supports Base Invoke Request
    """

    @property
    def input_object(self):
        pass

    @property
    def request_method(self) -> HttpsMethod: #pylint: disable=missing-function-docstring
        pass

    def send_request(self, value: Optional):  # pylint: disable=[signature-differs, missing-function-docstring]
        pass

    @property
    def invoke_request(self) -> Optional[Union[List[Entity], Entity]]:
        pass


class MockEntityRequestBuilder(AbstractEntityRequestBuilder):
    """
    Test Entity Request Builder
    """

    def request_with_options(self, options):
        pass


@pytest.fixture
def client() -> MockServiceClient:
    """Gets the testing client

    Returns:
        TestServiceClient: The testing client
    """
    return MockServiceClient()


@pytest.fixture
def entity_request_builder(
    client: MockServiceClient,  # pylint: disable=redefined-outer-name
) -> MockEntityRequestBuilder:
    """Gets the test entity request builder

    Args:
        client (TestServiceClient): The client

    Returns:
        TestEntityRequestBuilder: The test entity request builder
    """

    return MockEntityRequestBuilder("https://example.com", client)


@pytest.fixture
def base_request_builder(
    client: MockServiceClient,  # pylint: disable=redefined-outer-name
) -> MockBaseRequestBuilder:
    """Gets the test request builder

    Args:
        client (TestServiceClient): The client

    Returns:
        TestBaseRequestBuilder: The test request builder
    """

    return MockBaseRequestBuilder("https://example.com", client)


@pytest.fixture
def supports_base_invoke_request() -> MockSupportsBaseInvokeRequest:
    """Gets the test supports base invoke request

    Returns:
        TestSupportsBaseInvokeRequest: The test supports base invoke request
    """

    return MockSupportsBaseInvokeRequest()


def test_request_property(
    entity_request_builder: MockEntityRequestBuilder,
):  # pylint: disable=redefined-outer-name
    """Tests functionality of request

    Args:
        entity_request_builder (TestEntityRequestBuilder): The entity request builder
    """

    mock_request_with_options = MagicMock(return_value=BaseRequest)
    entity_request_builder.request_with_options = mock_request_with_options

    request = entity_request_builder.request

    assert request == BaseRequest
    mock_request_with_options.assert_called_once_with(None)


def test_base_request_builder_properties(
    base_request_builder: MockBaseRequestBuilder,  # pylint: disable=redefined-outer-name
    client: MockServiceClient,  # pylint: disable=redefined-outer-name
):
    """Tests changing request builder properties

    Args:
        base_request_builder (TestBaseRequestBuilder): The Test Base Request Builder
        client (TestServiceClient): The Test Client
    """

    assert base_request_builder.request_client == client
    assert base_request_builder.request_url == "https://example.com"

    base_request_builder.request_client = client
    base_request_builder.request_url = "https://newexample.com"

    assert base_request_builder.request_client == client
    assert base_request_builder.request_url == "https://newexample.com"


def test_base_request_builder_append_segment_to_request_url(
    base_request_builder: MockBaseRequestBuilder, # pylint: disable=redefined-outer-name
):
    """Tests Bas Request Builder's Append Segment to request url

    Args:
        base_request_builder (TestBaseRequestBuilder): The Test Base Request Builder
    """

    appended_url = base_request_builder.append_segment_to_request_url("segment")

    assert appended_url == "https://example.com/segment"


def test_supports_base_invoke_request_generic_type(
    supports_base_invoke_request: MockSupportsBaseInvokeRequest, # pylint: disable=redefined-outer-name
):
    """Tests if the generic type is set properly

    Args:
        supports_base_invoke_request (TestSupportsBaseInvokeRequest):
        The Supports Base Invoke Request
    """

    assert supports_base_invoke_request.generic_type == Entity
