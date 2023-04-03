"""
Tests Invoke Request
====================
"""
from typing import Optional, Union, List

import pytest

from pyrestsdk.type.model import Entity
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types._supports_base_invoke_request import (
    SupportsBaseInvokeRequest,
)


class TestEntity(Entity):
    pass


class TestSupportsBaseInvokeRequest(SupportsBaseInvokeRequest[TestEntity]):
    def __init__(self):
        self._input_object = TestEntity()
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
    test_instance = TestSupportsBaseInvokeRequest()
    assert isinstance(test_instance.input_object, TestEntity)


def test_request_method():
    test_instance = TestSupportsBaseInvokeRequest()
    assert test_instance.request_method == HttpsMethod.GET


def test_send():
    test_instance = TestSupportsBaseInvokeRequest()
    response = test_instance.send()
    assert isinstance(response, TestEntity)


def test_invoke_request():
    test_instance = TestSupportsBaseInvokeRequest()
    response = test_instance.invoke_request
    assert isinstance(response, TestEntity)
