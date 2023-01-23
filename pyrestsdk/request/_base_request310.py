"""Houses Base Request"""

from __future__ import annotations
from typing import (
    TypeVar,
    List,
    Union,
    Type,
    Optional,
    Iterable,
    Dict,
    Any,
)
from abc import abstractmethod
import logging
from urllib.parse import urlparse
import json
from requests import Response
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import (
    BaseEntity,
    QueryOption,
    HeaderOption,
)
from abc import abstractmethod
import logging
from requests import Response
from pyrestsdk.type.model import BaseEntity
from pyrestsdk.request._request import Request

Logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseEntity)
O = TypeVar("O", QueryOption, HeaderOption)


class BaseRequest(Request[T]):
    """The Base Request Type"""

    @abstractmethod
    def parse_response(
        self, _response: Optional[Response]
    ) -> Optional[Union[List[T], T]]:
        """Parses the response into the expected return"""

    def _parse_options(self, options: Optional[Iterable[O]]) -> None:
        """Parses the provided options into either header or query options"""

        Logger.info("%s._parse_options: function called", type(self).__name__)

        if options is None:
            return None

        for option in options:
            match type(option):
                case n if issubclass(n, HeaderOption):
                    self.header_options.append(option)
                case n if issubclass(n, QueryOption):
                    self.query_options.append(option)
                case other:
                    raise Exception(
                        "Unexpected type: %s, expected subtype of HeaderOption or QueryOption",
                        type(option),
                    )

    def _send_request(self, value: Optional[Union[T, Dict[str, Any]]]) -> Optional[Response]:
        """Makes the desired request and returns Response or None"""

        Logger.info(
            "%s._sendRequest: %s request made",
            type(self).__name__,
            self.request_method.name,
        )

        match self.request_method:
            case HttpsMethod.GET:
                return self._client.get(
                    url=self.request_url,
                    params=str(self.query_options),
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
                    data=json.dumps(value) if value is not None else None,
                )
            case other:
                raise Exception(f"Unknown HTTPS method {self.request_method.name}")


def parse_result(obj_type: Type[T], result: Dict, client) -> T:
    return obj_type(client).from_json(result)


def parse_result_list(obj_type: Type[T], results: List, client) -> List[T]:
    _results: List[T] = []

    for raw_result in results:
        _entry = obj_type(client).from_json(raw_result)
        _entry.__client = client
        _results.append(_entry)

    return _results
