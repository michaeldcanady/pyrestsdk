from __future__ import annotations
from typing import Optional, Union, List, TypeVar
from abc import abstractmethod
from pyrestsdk.type.model import BaseEntity
from pyrestsdk.request.supports_types._supports_types import SupportTypes

T = TypeVar("T", bound=BaseEntity)


class SupportsBaseInvokeRequest(SupportTypes):
    """Supports Base Invoke Request Type"""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request"""
