from __future__ import annotations
from typing import (
    Dict,
    TypeVar,
    List,
    Union,
    Type,
    Optional,
    Iterable,
)

from requests import Response

from abc import abstractmethod

import logging
from urllib.parse import urlparse
import json

# Internal Imports
from pyrestsdk import AbstractServiceClient
from pyrestsdk.request._abstract_request import AbstractRequest
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import (
    BaseEntity,
    QueryOption,
    HeaderOption,
    HeaderOptionCollection,
    QueryOptionCollection,
)

Logger = logging.getLogger(__name__)

S = TypeVar("S", bound="AbstractServiceClient")
T = TypeVar("T", bound="BaseEntity")
B = TypeVar("B", bound="BaseRequest")
O = TypeVar("O", QueryOption, HeaderOption)
H = TypeVar("H", bound=HeaderOption)
Q = TypeVar("Q", bound=QueryOption)


class BaseRequest(AbstractRequest[T]):
    """The Base Request Type"""
    
    def __init__(
        self: B, request_url: str, client: S, options: Optional[Iterable[O]]
    ) -> None:

        super().__init__(request_url, client)

        self._method: HttpsMethod = HttpsMethod.GET
        self._request_url: str = self._initialize_url(request_url)
        self._query_options: QueryOptionCollection = QueryOptionCollection()
        self._header_options: HeaderOptionCollection = HeaderOptionCollection()
        self._parse_options(options)

    @property
    def header_options(self) -> HeaderOptionCollection:
        """Gets the headers"""
        return self._header_options

    @property
    def request_method(self) -> HttpsMethod:
        """Gets/Sets the https method"""
        return self._method

    @request_method.setter
    def request_method(self, value: HttpsMethod) -> None:
        self._method = value
        Logger.info(f"{type(self).__name__}.Method: _method set to {value}")

    @property
    def query_options(self) -> QueryOptionCollection:
        """Gets the query options"""

        return self._query_options

    def _parse_options(self, options: Optional[Iterable[O]]) -> None:
        """Parses the provided options into either header or query options"""
        
        Logger.info(f"{type(self).__name__}._parse_options: function called")

        if options is None:
            return None

        for option in options:
            match type(option):
                case n if issubclass(n, HeaderOption):
                    self._header_options.append(option)
                case n if issubclass(n, QueryOption):
                    self._query_options.append(option)
                case other:
                    raise Exception(
                        "Unexpected type: %s, expected subtype of HeaderOption or QueryOption",
                        type(option),
                    )

    def _initialize_url(self, request_url: str) -> str:
        """Parses the query parameters from URL"""
        
        Logger.info(f"{type(self).__name__}._initialize_url: function called")

        if not request_url:
            pass

        url = urlparse(request_url)

        if url.query:
            queryString = url.query
            query_options = queryString.split("&")
            for option in query_options:
                query_parameter, value = option.split("=")
                _query_parameter = QueryOption(query_parameter, value)
                self.query_options.append(_query_parameter)

        return url._replace(query="").geturl()

    def Send(self, object: Optional[T]) -> Optional[Union[List[T], T]]:

        Logger.info(f"{type(self).__name__}.Send: method called")

        return self.send_request(object)

    def send_request(self, value: Optional[T]) -> Optional[Union[List[T], T]]:
        """Makes the desired request and returns the desired return type"""

        Logger.info(f"{type(self).__name__}.SendRequest: method called")

        _response = self._send_request(value)

        if _response is None:
            return None

        return self.parse_response(_response)

    @abstractmethod
    def parse_response(
        self, _response: Optional[Response]
    ) -> Optional[Union[List[T], T]]:
        """Parses the response into the expected return"""

    def _send_request(self, value: Optional[T]) -> Optional[Response]:
        """Makes the desired request and returns Response or None"""

        Logger.info(
            f"{type(self).__name__}._sendRequest: {self.request_method.name} request made"
        )

        match self.request_method:
            case HttpsMethod.GET:
                return self._client.get(
                    url=self.request_url, params=str(self.query_options)
                )
            case HttpsMethod.POST:
                return self._client.post(
                    url=self.request_url,
                    params=str(self.query_options),
                    data=json.dumps(value.Json) if value is not None else None,
                )
            case HttpsMethod.DELETE:
                self._client.delete(
                    url=self.request_url,
                    params=str(self.query_options),
                )
                return None
            case HttpsMethod.PUT:
                return self._client.put(
                    url=self.request_url,
                    params=str(self.query_options),
                    data=json.dumps(value.Json) if value is not None else None,
                )
            case other:
                raise Exception(f"Unknown HTTPS method {self.request_method.name}")


def parse_result(obj_type: Type[T], result: Dict, client) -> T:
    return obj_type(client).fromJson(result)


def parse_result_list(obj_type: Type[T], results: List, client) -> List[T]:
    _results: List[T] = []

    for raw_result in results:
        _entry = obj_type(client).fromJson(raw_result)
        _entry.__client = client
        _results.append(_entry)

    return _results
