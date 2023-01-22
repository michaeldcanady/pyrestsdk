"""Houses Base Request Builder"""

from __future__ import annotations
from typing import TypeVar
from logging import getLogger

from pyrestsdk import AbstractServiceClient
from pyrestsdk.requestbuilder._abstract_request_builder import AbstractRequestBuilder


S = TypeVar("S", bound=AbstractServiceClient)
B = TypeVar("B", bound="BaseRequestBuilder")

Logger = getLogger(__name__)


class BaseRequestBuilder(AbstractRequestBuilder):
    """Base Request Builder Type"""

    @property
    def Client(self: B) -> S:
        """Gets/Sets the Client"""

        Logger.info("%s.Client: get function called", type(self).__name__)

        return self._client

    @Client.setter
    def Client(self: B, client: S) -> None:

        Logger.info("%s.Client: set function called", type(self).__name__)

        self._client = client

        Logger.debug(
            "%s.request_url: request URL set to %s", type(self).__name__, client
        )

    @property
    def request_url(self: B) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """
        Logger.info("%s.request_url: get function called", type(self).__name__)

        return self._request_url

    @request_url.setter
    def request_url(self: B, value: str) -> None:

        Logger.info("%s.request_url: set function called", type(self).__name__)

        self._request_url = value

        Logger.debug(
            "%s.request_url: request URL set to %s", type(self).__name__, value
        )

    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """
        
        Logger.info("%s.append_segment_to_request_url: function called with %s", type(self).__name__, url_segment)

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self.request_url}{url_segment}"
