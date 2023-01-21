"""Houses Abstract Request Builder"""

from __future__ import annotations
from typing import (
    TypeVar,
    Generic,
    Type,
    final,
    get_args,
)
from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.model import (
    QueryOption,
    HeaderOption,
)

B = TypeVar("B", bound="AbstractRequestBuilder")
S = TypeVar("S", bound=AbstractServiceClient)
O = TypeVar("O", QueryOption, HeaderOption)
T = TypeVar("T")


class AbstractRequestBuilder(Generic[T]):
    """Abstract Request Type"""

    _client: S
    _request_url: str

    def __init__(self: B, request_url: str, client: S) -> None:

        super().__init__()

        self._request_url: str = request_url
        self._client = client

    @property
    def Client(self: B) -> S:
        """Gets the Client"""

        return self._client

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

    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self.request_url}{url_segment}"
