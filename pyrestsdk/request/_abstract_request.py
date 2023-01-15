"""Houses Abstract Request"""

from __future__ import annotations
from abc import abstractmethod
from typing import (
    List,
    Union,
    TypeVar,
    Generic,
    Type,
    final,
    get_args,
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
S = TypeVar("S", bound="AbstractServiceClient")
O = TypeVar("O", QueryOption, HeaderOption)
T = TypeVar("T")


class AbstractRequest(Generic[T]):
    """Abstract Request Type"""
    
    def __init__(self: B, request_url: str, client: S) -> None:

        super().__init__()

        self._request_url: str = request_url
        self._client: S = client

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
    def Client(self: B) -> S:
        return self._client

    @property
    @final
    def generic_type(self: B) -> Type[S]:
        """Gets the the type argument provided"""

        orig_classes = getattr(self, "__orig_class__", None)

        if orig_classes:
            return get_args(orig_classes)[0]

        _type: Type[S] = get_args(self.__orig_bases__[0])[0]  # type: ignore

        return _type

    @property
    def request_url(self: B) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """

        return self._request_url

    @request_url.setter
    def request_url(self: B, value: str) -> None:
        self._request_url = value

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

    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            # Checks if url segment starts with /
            # Appends it if it does not
            url_segment = "/{0}".format(url_segment)

        return "{0}{1}".format(self.request_url, url_segment)