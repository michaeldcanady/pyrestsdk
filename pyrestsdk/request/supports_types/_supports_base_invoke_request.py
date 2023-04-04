"""
Supports Base Invoke Request
============================
"""

from __future__ import annotations

from typing import Optional, Union, List, TypeVar

from abc import abstractmethod

from pyrestsdk.type.model import Entity
from pyrestsdk.request.supports_types._supports_types import SupportTypes
from pyrestsdk.request.supports_types._supports_generic_type import SupportsGenericType
from pyrestsdk.type.enum import HttpsMethod

T = TypeVar("T", bound=Entity)


class SupportsBaseInvokeRequest(SupportsGenericType[T], SupportTypes):
    """Supports Base Invoke Request Type"""

    @property
    @abstractmethod
    def input_object(self) -> Optional[T]:
        """Gets the input object for the request

        Returns:
            Optional[T]: _description_
        """
        raise NotImplementedError("input_object is not implemented")

    @property
    @abstractmethod
    def request_method(self) -> HttpsMethod:
        """Gets the Request HTTPS Method

        Returns:
            HttpsMethod: The Request HTTPS Method
        """
        raise NotImplementedError("request_method is not implemented")

    @abstractmethod
    def send(self, input_object: Optional[T] = None) -> Optional[Union[List[T], T]]:
        """Sends the request

        Args:
            input_object (Optional[T]): The input object to send. defaults to None

        Returns:
            Optional[Union[List[T], T]]: The response to the request
        """
        raise NotImplementedError("send is not implemented")

    @property
    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request

        Returns:
            Optional[Union[List[T], T]]: The response to the request
        """

        raise NotImplementedError("invoke_request is not implemented")
