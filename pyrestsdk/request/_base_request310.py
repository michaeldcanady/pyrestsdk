"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from __future__ import annotations

from typing import TypeVar, Union, Optional, Iterable, Dict, Any
import logging

from requests import Response

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import Entity, QueryOption, HeaderOption
from pyrestsdk.request._request import Request

Logger = logging.getLogger(__name__)

T = TypeVar("T", bound=Entity)


class BaseRequest(Request[T]): # pylint: disable=too-many-ancestors
    """
    Base Request
    ============
    
    """

    def _parse_options(
        self, options: Optional[Iterable[Union[QueryOption, HeaderOption]]]
    ) -> None:
        """Parses the provided options into either header or query options"""

        Logger.info("%s._parse_options: function called", type(self).__name__)

        if options is None:
            return None

        for option in options:
            if isinstance(option, HeaderOption):
                self.header_options.append(option)
            elif isinstance(option, QueryOption):
                self.query_options.append(option)
            else:
                raise TypeError(
                    f"Unexpected type: {type(option)}, expected instance of HeaderOption or QueryOption" #pylint: disable=line-too-long
                )
        return None

    def _send_request(self, args: Dict[str, Any]) -> Optional[Response]:
        """Sends request

        Args:
            args (Dict[str, Any]): _description_

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

        match self.request_method: #pylint: disable=syntax-error
            case HttpsMethod.GET: #pylint: disable=syntax-error
                return self._client.get(**args)
            case HttpsMethod.POST: #pylint: disable=syntax-error
                return self._client.post(**args)
            case HttpsMethod.DELETE: #pylint: disable=syntax-error
                self._client.delete(**args)
                return None
            case HttpsMethod.PUT: #pylint: disable=syntax-error
                return self._client.put(**args)
            case _: #pylint: disable=syntax-error
                raise TypeError(f"Unknown HTTPS method {self.request_method.name}")
