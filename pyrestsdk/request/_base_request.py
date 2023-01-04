from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Dict,
    TypeVar,
    Callable,
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
    Option,
    HeaderOptionCollection,
    QueryOptionCollection,
)

Logger = logging.getLogger(__name__)

S = TypeVar("S", bound="AbstractServiceClient")
T = TypeVar("T", bound="BaseEntity")
B = TypeVar("B", bound="BaseRequest")
O = TypeVar("O", bound=Option)
H = TypeVar("H", bound=HeaderOption)
Q = TypeVar("Q", bound=QueryOption)


class BaseRequest(AbstractRequest[T]):
    def __init__(
        self: B, request_url: str, client: S, options: Optional[Iterable[O]]
    ) -> None:

        super().__init__(request_url, client)

        self._method: HttpsMethod = HttpsMethod.GET
        self._request_url: str = self._initializeUrl(request_url)
        self._query_options: QueryOptionCollection = QueryOptionCollection()
        self._headers: HeaderOptionCollection = HeaderOptionCollection()
        self._parseOptions(options)

    @property
    def Headers(self) -> HeaderOptionCollection:
        """Gets the headers"""

        return self._headers

    @property
    def Method(self) -> HttpsMethod:
        """Gets/Sets the https method"""

        return self._method

    @Method.setter
    def Method(self, value: HttpsMethod) -> None:
        self._method = value
        Logger.info(f"{type(self).__name__}.Method: _method set to {value}")

    @property
    def QueryOptions(self) -> QueryOptionCollection:
        """Gets the query options"""

        return self._query_options

    def _parseOptions(self, options: Optional[Iterable[O]]) -> None:
        """Parses the provided options into either header or query options"""

        if options is None:
            return None

        for option in options:
            if issubclass(type(option), HeaderOption):
                self._headers.append(option)
            elif issubclass(type(option), QueryOption):
                self._query_options.append(option)
            else:
                raise Exception(
                    f"Unexpected type: {type(option)}, expected subtype of HeaderOption or QueryOption"
                )

    def _initializeUrl(self, request_url: str) -> str:
        """Parses the query parameters from URL"""

        if not request_url:
            pass

        url = urlparse(request_url)

        if url.query:
            queryString = url.query
            query_options = queryString.split("&")
            for option in query_options:
                query_parameter, value = option.split("=")
                _query_parameter = QueryOption(query_parameter, value)
                self.QueryOptions.append(_query_parameter)

        return url._replace(query="").geturl()

    def Send(self, object: Optional[T]) -> Optional[Union[List[T], T]]:

        Logger.info(f"{type(self).__name__}.Send: method called")

        return self.SendRequest(object)

    def SendRequest(self, value: Optional[T]) -> Optional[Union[List[T], T]]:
        """Makes the desired request and returns the desired return type"""

        Logger.info(f"{type(self).__name__}.SendRequest: method called")

        _response = self._sendRequest(value)

        if _response is None:
            return None

        return self.parse_response(_response)

    @abstractmethod
    def parse_response(
        self, _response: Optional[Response]
    ) -> Optional[Union[List[T], T]]:
        """Parses the response into the expected return"""

    def _sendRequest(self, value: Optional[T]) -> Optional[Response]:

        _request_dict: Dict[HttpsMethod, Callable] = {
            HttpsMethod.GET: self._client.get,
            HttpsMethod.POST: self._client.post,
            HttpsMethod.DELETE: self._client.delete,
            HttpsMethod.PUT: self._client.put,
        }

        Logger.info(
            f"{type(self).__name__}._sendRequest: {self.Method.name} request made"
        )

        _func = _request_dict.get(self.Method, None)

        if _func is None:
            raise Exception(f"Unknown HTTPS method {self.Method.name}")

        _response = _func(
            url=self.RequestUrl,
            params=str(self._query_options),
            data=json.dumps(value.Json) if value is not None else None,
        )

        if self.Method == HttpsMethod.DELETE:
            return None

        return _response


def parse_result(obj_type: Type[T], result: Dict, client) -> T:
    return obj_type(client).fromJson(result)


def parse_result_list(obj_type: Type[T], results: List, client) -> List[T]:
    _results: List[T] = []

    for raw_result in results:
        _entry = obj_type(client).fromJson(raw_result)
        _entry.__client = client
        _results.append(_entry)

    return _results
