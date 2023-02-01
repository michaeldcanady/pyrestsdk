"""Houses Abstract Request Builder"""

from __future__ import annotations
from typing import (
    TypeVar,
    Generic,
)
from abc import abstractmethod, ABC
from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.model import (
    QueryOption,
    HeaderOption,
)

B = TypeVar("B", bound="AbstractRequestBuilder")
S = TypeVar("S", bound=AbstractServiceClient)
O = TypeVar("O", QueryOption, HeaderOption)
T = TypeVar("T")


class AbstractRequestBuilder(ABC, Generic[T]):
    """Abstract Request Type"""

    _client: S
    _request_url: str

    @abstractmethod
    def __init__(self: B, request_url: str, client: S) -> None:
        """Instantiates new object"""

    @property
    @abstractmethod
    def request_client(self: B) -> S:
        """Gets/Sets the Client"""

    @property
    @abstractmethod
    def request_url(self: B) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """

    @abstractmethod
    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """
