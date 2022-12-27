from __future__ import annotations
from typing import Type, Iterable, TypeVar
from abc import abstractmethod

# internal imports
from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.model import BaseEntity, Option
from pyrestsdk.request import BaseRequest

T = TypeVar("T", bound="BaseEntity")
B = TypeVar("B", bound="BaseRequest")
O = TypeVar("O", bound=Option)
S = TypeVar("S", bound="AbstractServiceClient")


class InvokableRequest(BaseRequest):
    def __init__(
        self: B,
        _return_type: Type[T],
        request_url: str,
        client: S,
        options: Iterable[O],
    ) -> None:
        super().__init__(_return_type, request_url, client, options)

    @abstractmethod
    def Invoke(self):...
