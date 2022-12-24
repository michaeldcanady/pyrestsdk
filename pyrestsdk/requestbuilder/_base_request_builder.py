from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Dict,
    TypeVar,
    Callable,
    List,
    Union,
    Type,
    Optional,
    Iterable,
)

# Internal Imports
from pyrestsdk import AbstractServiceClient
from pyrestsdk.request._abstract_request import AbstractRequest

S = TypeVar("S", bound="AbstractServiceClient")
B = TypeVar("B", bound="BaseRequestBuilder")

class BaseRequestBuilder(AbstractRequest):

    def __init__(self: B, request_url: str, client: S) -> None:
        super().__init__(request_url, client)