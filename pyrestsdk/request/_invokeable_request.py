from __future__ import annotations
from typing import Type, Iterable, TypeVar, Optional, Union, List
from abc import abstractmethod

# internal imports
from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.model import BaseEntity, HeaderOption, QueryOption
from pyrestsdk.request import BaseRequest

T = TypeVar("T", bound="BaseEntity")
B = TypeVar("B", bound="BaseRequest")
O = TypeVar("O", HeaderOption, QueryOption)
S = TypeVar("S", bound="AbstractServiceClient")


class InvokableRequest(BaseRequest[T]):
    def __init__(
        self: B,
        request_url: str,
        client: S,
        options: Optional[Iterable[O]],
    ) -> None:
        super().__init__(request_url, client, options)

    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request
        """
