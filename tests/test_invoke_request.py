from pyrestsdk.type.model import Entity
from pyrestsdk.request.supports_types import SupportsBaseInvokeRequest
from pyrestsdk.type.enum import HttpsMethod
from typing import List, TypeVar, Optional, Union
import pytest

Entity = TypeVar("Entity", bound=Entity)


class MockSupportsBaseInvokeRequest(SupportsBaseInvokeRequest[Entity]):
    def __init__(self, method: HttpsMethod):

        super().__init__()
        self.method = method

    def send(self, obj: Optional[Union[Entity, List[Entity]]]):
        pass

    @property
    def input_object(self):
        pass

    @property
    def request_method(self) -> HttpsMethod:
        return self.method

    @property
    def invoke_request(self) -> Optional[Union[List[Entity], Entity]]:
        pass


def test_supports_base_invoke_request_generic_type():
    mock_request = MockSupportsBaseInvokeRequest(HttpsMethod.GET)
    assert mock_request.generic_type == Entity


def test_supports_base_invoke_request_method():
    mock_request = MockSupportsBaseInvokeRequest(HttpsMethod.GET)
    assert mock_request.request_method == HttpsMethod.GET


def test_supports_base_invoke_request_send():
    mock_request = MockSupportsBaseInvokeRequest(HttpsMethod.GET)
    assert mock_request.send("some_string") == None
    assert mock_request.send({"some_key": "some_value"}) == None


def test_supports_base_invoke_request_invoke_request():
    mock_request = MockSupportsBaseInvokeRequest(HttpsMethod.GET)
    assert mock_request.invoke_request == None
