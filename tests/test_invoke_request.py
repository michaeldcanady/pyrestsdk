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


class MockEntity(Entity):
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


class MockClient(ServiceClient):
    """
    Test Client
    """

    def _get_session(self): #pylint: disable=arguments-differ
        pass

    @staticmethod
    def _initialize_session_and_base_url(*args, **kwargs):
        pass


class MockSupportsBaseInvokeRequest(SupportsBaseInvokeRequest[MockEntity]): #pylint: disable=too-many-ancestors
    """
    Test Supports Base Invoke Request
    """

    def __init__(self):
        super().__init__()
        self._input_object = MockEntity(MockClient())
        self._request_method = HttpsMethod.GET

    @property
    def input_object(self) -> Optional[MockEntity]:
        return self._input_object

    @property
    def request_method(self) -> HttpsMethod: #pylint: disable=missing-function-docstring
        return self._request_method

    def send_request(
        self, value: Optional[MockEntity] = None
    ) -> Optional[Union[List[MockEntity], MockEntity]]:
        return value

    @property
    def invoke_request(self) -> Optional[Union[List[MockEntity], MockEntity]]:
        return self.send_request(self._input_object)


def test_input_object():
    """
    Tests if input object is set property
    """

    test_instance = MockSupportsBaseInvokeRequest()
    assert isinstance(test_instance.input_object, MockEntity)


def test_request_method():
    """
    Tests if base request_method is GET
    """
    test_instance = MockSupportsBaseInvokeRequest()
    assert test_instance.request_method == HttpsMethod.GET


def test_send():
    """
    Tests send with no object input
    """

    test_instance = MockSupportsBaseInvokeRequest()
    response = test_instance.send_request()
    assert isinstance(response, MockEntity)


def test_invoke_request():
    """
    Tests if invoke_request returns response
    """

    test_instance = MockSupportsBaseInvokeRequest()
    response = test_instance.invoke_request
    assert isinstance(response, MockEntity)


