"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from typing import TypeVar, Optional, Dict, Any, Union, List

from abc import ABC, abstractmethod

from pyrestsdk.type.model import Entity
from pyrestsdk.request.supports_types._supports_types import SupportTypes

T = TypeVar("T", bound=Entity)
S = TypeVar("S", bound="SupportsInvokeRequest")

class SupportsSendRequest(SupportTypes, ABC):
    """
    Supports Invoke Request
    =======================
    
    Request supports invokation at later time
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self._input_object = None

    @property
    @abstractmethod
    def input_object(self) -> Optional[T]:
        """_summary_

        Returns:
            Optional[T]: _description_
        """

    @abstractmethod
    def send_request(
        self, value: Optional[Union[T, Dict[str, Any]]] = None
    ) -> Optional[Union[List[T], T]]:
        """Makes the desired request and returns the desired return type"""
