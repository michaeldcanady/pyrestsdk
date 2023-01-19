"""Houses Entity Request Builder"""

from __future__ import annotations
from typing import TypeVar, Iterable, Optional
from abc import abstractmethod
from pyrestsdk import AbstractServiceClient
from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.request import BaseRequest
from pyrestsdk.type.model import Option

S = TypeVar("S", bound=AbstractServiceClient)
B = TypeVar("B", bound=BaseRequestBuilder)
R = TypeVar("R", bound=BaseRequest)
O = TypeVar("O", bound=Option)


class EntityRequestBuilder(BaseRequestBuilder):
    """Entity Request Builder Type"""

    @property
    @abstractmethod
    def request(self: B) -> R:
        """Gets request with no options"""

    @abstractmethod
    def Request(self: B, options: Optional[Iterable[O]]) -> R:
        """Gets request"""
