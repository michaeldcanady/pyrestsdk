"""Houses Invokable Request"""

from __future__ import annotations
from typing import TypeVar, Optional, Union, List
from abc import abstractmethod
from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.model import BaseEntity, HeaderOption, QueryOption
from pyrestsdk.request import BaseRequest

T = TypeVar("T", bound=BaseEntity)
B = TypeVar("B", bound=BaseRequest)
O = TypeVar("O", HeaderOption, QueryOption)
S = TypeVar("S", bound=AbstractServiceClient)


class InvokableRequest(BaseRequest[T]):
    """Invokable Request Type"""

    @abstractmethod
    def invoke_request(self) -> Optional[Union[List[T], T]]:
        """Invokes the prepared request
        """
