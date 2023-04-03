"""Houses Request Type
"""

from typing import TypeVar, List, Union, Optional, Iterable, Dict, Any
import logging
from urllib.parse import urlparse
import json

from pyrestsdk import AbstractServiceClient
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import Entity, QueryOption, HeaderOption
from pyrestsdk.request._abstract_request import AbstractRequest
from pyrestsdk.request.supports_types import (
    SupportsGenericType,
    SupportsQueryOptions,
    SupportsHeaderOptions,
)

T = TypeVar("T", bound=Entity)
S = TypeVar("S", bound=AbstractServiceClient)

Logger = logging.getLogger(__name__)


class Request( #pylint: disable=too-many-ancestors
    SupportsHeaderOptions,
    SupportsQueryOptions,
    SupportsGenericType,
    AbstractRequest[T],
):
    """Request Type"""

    def __init__(
        self,
        request_url: str,
        client: S,
        options: Optional[Iterable[Union[QueryOption, HeaderOption]]],
    ) -> None:
        super().__init__(request_url, client, options)

        self._request_url: str = request_url
        self._client: S = client
        self._method: HttpsMethod = HttpsMethod.GET
        self._request_url: str = self._initialize_url(request_url)
        self._parse_options(options)

    @property
    def request_method(self) -> HttpsMethod:
        """Gets/Sets the HTTPS method

        Returns:
            HttpsMethod: The HTTPS method
        """

        return self._method

    @request_method.setter
    def request_method(self, value: HttpsMethod) -> None:
        self._method = value
        Logger.info("%s.Method: request method set to %s", type(self).__name__, value)

    @property
    def request_url(self) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """

        return self._request_url

    @request_url.setter
    def request_url(self, value: str) -> None:
        self._request_url = value
        Logger.info("%s.request_url: request URL set to %s", type(self).__name__, value)

    @property
    def client(self) -> S:
        """Gets the Client"""

        return self._client

    def _initialize_url(self, request_url: str) -> str:
        """Parses the query parameters from URL"""

        Logger.info("%s._initialize_url: function called", type(self).__name__)

        if not request_url:
            raise TypeError("request url can't be None")

        url = urlparse(request_url)

        if url.query:
            self._split_query_options(url.query)

        return url._replace(query="").geturl()

    def send(
        self, value: Optional[Union[T, Dict[str, Any]]] = None
    ) -> Optional[Union[List[T], T]]:
        """Makes the desired request and returns the desired return type"""

        Logger.info("%s.Send: method called", type(self).__name__)

        args = self._get_request_args(value)

        response = self._send_request(args, value)

        if response is None:
            return None

        try:
            Logger.debug("%s.Send: raising response for status", type(self).__name__)
            response.raise_for_status()
        except Exception: #pylint: disable=broad-exception-caught
            return self.parse_exception(response)
        return self.parse_response(response)

    def _parse_input_object(self, input_value: Union[T, Dict[str, Any], str]) -> str:
        """Converts input object into JSON

        Args:
            input_value (Union[T, Dict[str, Any], str]): The input object

        Returns:
            str: JSON version of object
        """

        if isinstance(input_value, str):
            return input_value

        if not isinstance(input_value, dict):
            input_value = input_value.as_dict

        return json.dumps(input_value)

    def _get_request_args( #pylint: disable=arguments-renamed
        self, input_value: Optional[Union[T, Dict[str, Any], str]] = None
    ) -> Dict[str, Any]:
        args = {
            "url": self.request_url,
            "headers": self.header_options.as_dict,
            "params": str(self.query_options),
        }

        if self.request_method in (HttpsMethod.POST, HttpsMethod.PUT):
            if input_value is None:
                raise ValueError(f"Missing data for {self.request_method.name} request.")

            args["data"] = self._parse_input_object(input_value)

        return args

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
