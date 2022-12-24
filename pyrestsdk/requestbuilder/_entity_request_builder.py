from __future__ import annotations

from typing import TypeVar, Iterable
from abc import abstractmethod

# internal imports
from pyrestsdk import AbstractServiceClient
from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.request._base_request import BaseRequest
from pyrestsdk.type.model import Option

S = TypeVar("S", bound="AbstractServiceClient")
B = TypeVar("B", bound="BaseRequestBuilder")
R = TypeVar("R", bound=BaseRequest)
O = TypeVar("O", bound=Option)

class EntityRequestBuilder(BaseRequestBuilder):

    def __init__(self: B, request_url: str, client: S) -> None:
        super().__init__(request_url, client)

    @property
    def request(self: B) -> R:

        return self.Request(None)

    def Request(self: B, options: Iterable[O]) -> R:

        return BaseRequest(self.RequestUrl, self.Client, options)