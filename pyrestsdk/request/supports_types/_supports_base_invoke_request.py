"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from __future__ import annotations

from typing import Optional, Union, List, TypeVar

from abc import abstractmethod

from pyrestsdk.type.model import Entity
from pyrestsdk.request.supports_types._supports_types import SupportTypes
from pyrestsdk.request.supports_types._supports_generic_type import SupportsGenericType
from pyrestsdk.request.supports_types._supports_send_request import SupportsSendRequest

T = TypeVar("T", bound=Entity)


class SupportsBaseInvokeRequest(SupportsGenericType[T], SupportsSendRequest, SupportTypes):
    """
    Supports Base Invoke Request
    ============================
    
    
    """

    @property
    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request

        Returns:
            Optional[Union[List[T], T]]: The response to the request
        """

        raise NotImplementedError("invoke_request is not implemented")
