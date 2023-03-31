"""Houses Base Request"""

from __future__ import annotations

from typing import TypeVar, Union, Optional, Iterable, Dict, Any
import logging

from requests import Response

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import Entity, QueryOption, HeaderOption
from pyrestsdk.request._request import Request

Logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Entity)


class BaseRequest(Request[T]):
    """The Base Request Type"""

    def _parse_options(self, options: Optional[Iterable[Union[QueryOption, HeaderOption]]]) -> None:
        """Parses the provided options into either header or query options"""

        Logger.info("%s._parse_options: function called", type(self).__name__)

        if options is None:
            return None

        for option in options:
            if isinstance(option, HeaderOption):
                self.header_options.append(option)
                print(len(self.header_options))
            elif isinstance(option, QueryOption):
                self.query_options.append(option)
            else:
                raise TypeError(
                    f"Unexpected type: {type(option)}, expected instance of HeaderOption or QueryOption"
                )

    def _send_request(self, args: Dict[str, Any], value: Optional[Union[T, Dict[str, Any], str]]) -> Optional[Response]:
        """Sends request

        Args:
            args (Dict[str, Any]): _description_
            value (Optional[Union[T, Dict[str, Any], str]]): _description_

        Raises:
            Exception: _description_

        Returns:
            Optional[Response]: Response to request
        """

        Logger.info(
            "%s._send_request: %s request made",
            type(self).__name__,
            self.request_method.name,
        )

        match self.request_method:
            case HttpsMethod.GET:
                return self._client.get(**args)
            case HttpsMethod.POST:
                return self._client.post(**args)
            case HttpsMethod.DELETE:
                self._client.delete(**args)
                return None
            case HttpsMethod.PUT:
                return self._client.put(**args)
            case _:
                raise TypeError(f"Unknown HTTPS method {self.request_method.name}")
