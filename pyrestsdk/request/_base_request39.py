"""Houses Base Request"""

from __future__ import annotations
from typing import (
    TypeVar,
    List,
    Union,
    Type,
    Optional,
    Iterable,
    Callable,
    Dict,
    Any,
)
from abc import abstractmethod
import logging
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

    def _send_request(self, value: Optional[Union[T, Dict[str, Any]]]) -> Optional[Response]:
        _request_dict: Dict[HttpsMethod, Callable] = {
            HttpsMethod.GET: self._client.get,
            HttpsMethod.POST: self._client.post,
            HttpsMethod.DELETE: self._client.delete,
            HttpsMethod.PUT: self._client.put,
        }

        Logger.info(
            f"{type(self).__name__}._sendRequest: {self.request_method.name} request made"
        )

        _func = _request_dict.get(self.request_method, None)

        if _func is None:
            raise Exception(f"Unknown HTTPS method {self.request_method.name}")
        
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


def parse_result(obj_type: Type[T], result: Dict, client) -> T:
    return obj_type(client).from_json(result)


def parse_result_list(obj_type: Type[T], results: List, client) -> List[T]:
    _results: List[T] = []

    for raw_result in results:
        _entry = obj_type(client).from_json(raw_result)
        _entry.__client = client
        _results.append(_entry)

    return _results
