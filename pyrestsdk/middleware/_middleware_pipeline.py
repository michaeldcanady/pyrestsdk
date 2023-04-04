"""Houses Middleware Pipeline"""

from typing import TypeVar
import json
import ssl
from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager
from pyrestsdk.middleware._base_middleware import BaseMiddleware
from pyrestsdk.middleware._request_context import RequestContext

B = TypeVar("B", bound=BaseMiddleware)


class MiddlewarePipeline(HTTPAdapter):
    """MiddlewarePipeline, entry point of middleware
    The pipeline is implemented as a linked-list, read more about
    it here https://buffered.dev/middleware-python-requests/
    """

    def __init__(self) -> None:
        super().__init__()
        self._current_middleware = None
        self._first_middleware = None
        self.poolmanager = PoolManager(ssl_version=ssl.PROTOCOL_TLSv1_2)

    def add_middleware(self, middleware: B) -> None:
        """Adds middleware to the pipeline"""

        if (not isinstance(middleware, BaseMiddleware)) or (
            not issubclass(type(middleware), BaseMiddleware)
        ):
            raise TypeError(
                f"middleware is not of or subtype of {BaseMiddleware.__name__!r} is {type(middleware).__name__!r}" #pylint: disable=line-too-long
            )

        if self._current_middleware is not None:
            self._current_middleware.next = middleware
            self._current_middleware = middleware
        else:
            self._first_middleware = middleware
            self._current_middleware = self._first_middleware

    def send( #pylint: disable=too-many-arguments
        self,
        request: PreparedRequest,
        stream: bool = False,
        timeout=None,
        verify: bool = True,
        cert=None,
        proxies=None,
    ) -> Response:
        """Sends the prepared request through the middleware pipeline"""

        if request is None:
            raise TypeError("request cannot be None")

        if request.headers is None:
            request.headers = {}

        middleware_control_json = request.headers.pop("middleware_control", None)

        if middleware_control_json:
            middleware_control = json.loads(middleware_control_json)
        else:
            middleware_control = {}

        # Set Context
        request.context = RequestContext(middleware_control, request.headers)

        if self._first_middleware is None:
            # No middleware in pipeline, call superclass' send
            return super().send(request, stream, timeout, verify, cert, proxies)

        return self._first_middleware.send(
            request, stream, timeout, verify, cert, proxies
        )
