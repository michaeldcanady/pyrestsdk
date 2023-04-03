from typing import Optional, Union, List

from unittest.mock import MagicMock

import pytest

from requests import Session

from pyrestsdk import AbstractServiceClient
from pyrestsdk.requestbuilder._entity_request_builder import EntityRequestBuilder as AbstractEntityRequestBuilder
from pyrestsdk.request import BaseRequest
from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.request.supports_types._supports_base_invoke_request import SupportsBaseInvokeRequest
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import Entity


class TestServiceClient(AbstractServiceClient):
    """
    Service Client for testing
    """

    def __init__(self):
        self.session = Session()

    def _get_session(self): #pylint: disable=arguments-differ
        return self.session

    def _instance_url(self): #pylint: disable=arguments-differ
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

class TestBaseRequestBuilder(BaseRequestBuilder):
    pass

class TestSupportsBaseInvokeRequest(SupportsBaseInvokeRequest[Entity]):
    @property
    def input_object(self):
        pass

    @property
    def request_method(self) -> HttpsMethod:
        pass

    def send(self, obj: Optional):
        pass

    @property
    def invoke_request(self) -> Optional[Union[List[Entity], Entity]]:
        pass


class TestEntityRequestBuilder(AbstractEntityRequestBuilder):
    def request_with_options(self, options):
        pass


@pytest.fixture
def client() -> TestServiceClient:
    """Gets the testing client

    Returns:
        TestServiceClient: The testing client
    """
    return TestServiceClient()


@pytest.fixture
def entity_request_builder(client: TestServiceClient) -> TestEntityRequestBuilder: #pylint: disable=redefined-outer-name
    """Gets the test entity request builder

    Args:
        client (TestServiceClient): The client

    Returns:
        TestEntityRequestBuilder: The test entity request builder
    """

    return TestEntityRequestBuilder("https://example.com", client)

@pytest.fixture
def base_request_builder(client: TestServiceClient) -> TestBaseRequestBuilder: #pylint: disable=redefined-outer-name
    """Gets the test request builder

    Args:
        client (TestServiceClient): The client

    Returns:
        TestBaseRequestBuilder: The test request builder
    """

    return TestBaseRequestBuilder("https://example.com", client)

@pytest.fixture
def supports_base_invoke_request() -> TestSupportsBaseInvokeRequest:
    """Gets the test supports base invoke request

    Returns:
        TestSupportsBaseInvokeRequest: The test supports base invoke request
    """

    return TestSupportsBaseInvokeRequest()


def test_request_property(entity_request_builder: TestEntityRequestBuilder): #pylint: disable=redefined-outer-name
    """Tests functionality of request

    Args:
        entity_request_builder (TestEntityRequestBuilder): The entity request builder
    """

    mock_request_with_options = MagicMock(return_value=BaseRequest)
    entity_request_builder.request_with_options = mock_request_with_options

    request = entity_request_builder.request

    assert request == BaseRequest
    mock_request_with_options.assert_called_once_with(None)

def test_base_request_builder_properties(base_request_builder: TestBaseRequestBuilder, client: TestServiceClient): #pylint: disable=redefined-outer-name 
    assert base_request_builder.request_client == client
    assert base_request_builder.request_url == "https://example.com"

    base_request_builder.request_client = client
    base_request_builder.request_url = "https://newexample.com"

    assert base_request_builder.request_client == client
    assert base_request_builder.request_url == "https://newexample.com"

def test_base_request_builder_append_segment_to_request_url(base_request_builder):
    appended_url = base_request_builder.append_segment_to_request_url("segment")

    assert appended_url == "https://example.com/segment"

def test_supports_base_invoke_request_generic_type(supports_base_invoke_request):
    assert supports_base_invoke_request.generic_type == Entity
