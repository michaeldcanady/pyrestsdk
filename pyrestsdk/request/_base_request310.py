"""Houses Base Request"""

from __future__ import annotations

from typing import (
    TypeVar,
    Union,
    Optional,
    Iterable,
    Dict,
    Any,
)

import logging

import json

from requests import Response

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import (
    Entity,
    QueryOption,
    HeaderOption,
)

from pyrestsdk.request._request import Request

Logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Entity)
Q = TypeVar("Q", bound=QueryOption)
H = TypeVar("H", bound=HeaderOption)


class BaseRequest(Request[T]):
    """The Base Request Type"""

    def _parse_options(self, options: Optional[Iterable[Union[Q, H]]]) -> None:
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
            "%s._send_request: %s request made",
            type(self).__name__,
            self.request_method.name,
        )
        
        if not isinstance(value, dict) and value is not None:
            value = value.as_dict
        

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
                    data=json.dumps(value) if value is not None else None,
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