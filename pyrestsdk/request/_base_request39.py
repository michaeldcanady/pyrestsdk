"""Houses Base Request"""

from __future__ import annotations

from typing import (
    TypeVar,
    Union,
    Optional,
    Iterable,
    Callable,
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
from pyrestsdk.type.model import Entity
from pyrestsdk.request._request import Request

Logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Entity)
O = TypeVar("O", QueryOption, HeaderOption)


class BaseRequest(Request[T]):
    """The Base Request Type"""

    def _parse_options(self, options: Optional[Iterable[O]]) -> None:
        """Parses the provided options into either header or query options"""

        if options is None:
            return None

        for option in options:
            if issubclass(type(option), HeaderOption):
                self.header_options.append(option)
            elif issubclass(type(option), QueryOption):
                self.query_options.append(option)
            else:
                raise Exception(
                    "Unexpected type: %s, expected subtype of HeaderOption or QueryOption",
                    type(option),
                )

        return None

    def _send_request(
        self, value: Optional[Union[T, Dict[str, Any]]]
    ) -> Optional[Response]:
        _request_dict: Dict[HttpsMethod, Callable] = {
            HttpsMethod.GET: self._client.get,
            HttpsMethod.POST: self._client.post,
            HttpsMethod.DELETE: self._client.delete,
            HttpsMethod.PUT: self._client.put,
        }

        Logger.info(
            "%s._sendRequest: %s request made",
            type(self).__name__,
            self.request_method.name,
        )

        _func = _request_dict.get(self.request_method, None)

        if _func is None:
            raise Exception("Unknown HTTPS method: %s", self.request_method.name)

        _value = None

        if self.request_method == HttpsMethod.PUT:
            _value = value
        else:
            _value = json.dumps(value.as_json) if value is not None else None

        _response = _func(
            url=self.request_url,
            params=str(self._query_options),
            data=_value,
        )

        if self.request_method == HttpsMethod.DELETE:
            return None

        return _response
