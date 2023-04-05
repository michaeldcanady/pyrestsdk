"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List, Union, TypeVar, Generic, Optional, Iterable, Dict, Any

from requests import Response

from pyrestsdk import ServiceClient

from pyrestsdk.type.enum import HttpsMethod

from pyrestsdk.type.model import (
    CommonBase,
    QueryOption,
    HeaderOption,
    HeaderOptionCollection,
    QueryOptionCollection,
)

B = TypeVar("B", bound="AbstractRequest")
S = TypeVar("S", bound=ServiceClient)
O = TypeVar("O", QueryOption, HeaderOption)
T = TypeVar("T")


class AbstractRequest(
    CommonBase,
    Generic[T],
    ABC,
):
    """
    Abstract Request
    ================
    
    """

    @abstractmethod
    def __init__(
        self: B, request_url: str, client: S, options: Optional[Iterable[O]]
    ) -> None:
        """Instantiates new request"""
        super().__init__()

    @property
    @abstractmethod
    def header_options(self) -> HeaderOptionCollection:
        """Gets the headers"""

    @property
    @abstractmethod
    def request_method(self) -> HttpsMethod:
        """Gets/Sets the https method"""

    @property
    @abstractmethod
    def query_options(self) -> QueryOptionCollection:
        """Gets the query options"""

    @property
    @abstractmethod
    def client(self: B) -> S:
        """Gets the Client"""

    @property
    @abstractmethod
    def request_url(self: B) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """

    @abstractmethod
    def _parse_options(self, options: Optional[Iterable[O]]) -> None:
        """Parses the provided options into either header or query options"""

    @abstractmethod
    def _initialize_url(self, request_url: str) -> str:
        """Parses the query parameters from URL"""

    @abstractmethod
    def parse_response(
        self, _response: Optional[Response]
    ) -> Optional[Union[List[T], T]]:
        """Parses the response into the expected return"""

    @abstractmethod
    def _get_request_args(
        self, value: Optional[Union[T, Dict[str, Any], str]] = None
    ) -> Dict[str, Any]:
        """gets request arguments"""

    @abstractmethod
    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """

    @abstractmethod
    def parse_exception(self, response: Response) -> None:
        """Raises exception based off response"""
