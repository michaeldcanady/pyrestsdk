"""
Tests Invoke Request
====================
"""
from typing import Optional, Union, List

from pyrestsdk.type.model import Entity
from pyrestsdk import ServiceClient
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types._supports_base_invoke_request import (
    SupportsBaseInvokeRequest,
)


class TestEntity(Entity):
    """
    Test Entity
    """
    @property
    def as_dict(self):
        pass

    @property
    def as_json(self):
        pass

    @staticmethod
    def from_json(entry):
        pass
    

class TestClient(ServiceClient):
    """
    Test Client
    """

    def _get_session():
        pass


class TestSupportsBaseInvokeRequest(SupportsBaseInvokeRequest[TestEntity]):
    """
    Test Supports Base Invoke Request
    """

    def __init__(self):
        super().__init__()
        self._input_object = TestEntity(TestClient())
        self._request_method = HttpsMethod.GET

    @property
    def input_object(self) -> Optional[TestEntity]:
        return self._input_object

    @property
    def request_method(self) -> HttpsMethod:
        return self._request_method

    def send(
        self, input_object: Optional[TestEntity] = None
    ) -> Optional[Union[List[TestEntity], TestEntity]]:
        return self._input_object

    @property
    def invoke_request(self) -> Optional[Union[List[TestEntity], TestEntity]]:
        return self.send()


def test_input_object():
    """
    Tests if input object is set property
    """

    test_instance = TestSupportsBaseInvokeRequest()
    assert isinstance(test_instance.input_object, TestEntity)


def test_request_method():
    """
    Tests if base request_method is GET
    """
    test_instance = TestSupportsBaseInvokeRequest()
    assert test_instance.request_method == HttpsMethod.GET


def test_send():
    """
    Tests send with no object input
    """

    test_instance = TestSupportsBaseInvokeRequest()
    response = test_instance.send()
    assert isinstance(response, TestEntity)


def test_invoke_request():
    """
    Tests if invoke_request returns response
    """

    test_instance = TestSupportsBaseInvokeRequest()
    response = test_instance.invoke_request
    assert isinstance(response, TestEntity)
