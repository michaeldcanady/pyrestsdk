from __future__ import annotations
from typing import Protocol, Optional, Union, List, TypeVar, Type
from abc import abstractmethod
from pyrestsdk.type.model import BaseEntity

T = TypeVar("T", bound=BaseEntity)


class SupportsBaseInvokeRequest(Protocol):
    """Supports Base Invoke Request Type"""

    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request"""
