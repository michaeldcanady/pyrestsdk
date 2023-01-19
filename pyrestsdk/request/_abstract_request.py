"""Houses Abstract Request"""

from __future__ import annotations
from abc import abstractmethod
from typing import (
    List,
    Union,
    TypeVar,
    Generic,
    Type,
    Optional,
    Iterable,
)
from requests import Response
from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import (
    QueryOption,
    HeaderOption,
    HeaderOptionCollection,
    QueryOptionCollection,
)

B = TypeVar("B", bound="AbstractRequest")
S = TypeVar("S", bound=AbstractServiceClient)
O = TypeVar("O", QueryOption, HeaderOption)
T = TypeVar("T")


class AbstractRequest(Generic[T]):
    """Abstract Request Type"""

    _request_url: str
    _client: S

    def __init__(self: B, request_url: str, client: S) -> None:

        super().__init__()

        self._request_url = request_url
        self._client = client

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
    def Client(self: B) -> S:
        """Gets the Client"""

    @property
    @abstractmethod
    def generic_type(self: B) -> Type[T]:
        """Gets the the type argument provided"""

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
    def send_request(self, value: Optional[T]) -> Optional[Union[List[T], T]]:
        """Makes the desired request and returns the desired return type"""

    @abstractmethod
    def _send_request(self, value: Optional[T]) -> Optional[Response]:
        """Makes the desired request and returns Response or None"""

    @abstractmethod
    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """
