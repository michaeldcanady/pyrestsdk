"""Houses Client Factory"""
from typing import TypeVar, List, Type
from logging import getLogger

from requests import Session

from pyrestsdk.middleware import MiddlewarePipeline
from pyrestsdk.middleware import BaseMiddleware
from pyrestsdk.credential import AbstractBasicCredential
from pyrestsdk.clientfactory._abstract_client_factory import AbstractHTTPClientFactory

Logger = getLogger(__name__)

B = TypeVar("B", bound=BaseMiddleware)
C = TypeVar("C", bound=AbstractBasicCredential)


class HTTPClientFactory(AbstractHTTPClientFactory):
    """HTTP Client Factory"""

    def __init__(
        self,
        base_url: str,
        session: Session,
        protocol: str = "https",
    ) -> None:
        super().__init__(session)
        self._base_url = base_url
        self._protocol = protocol

    def create_with_custom_middleware(self, middleware: List[B]) -> Session:

        if not middleware:
            raise ValueError("Please provide a list of custom middleware")

        return self._register(middleware)

    def _set_base_url(self, sub_domain: str) -> None:

        Logger.info("%s._set_base_url(): method called", type(self).__name__)

        self.session.base_url = f"{self._protocol}://{sub_domain}.{self._base_url}" # type: ignore

        Logger.debug(
            "%s._set_base_url() : base url set to: %s",
            type(self),
            self.session.base_url, # type: ignore
        )

        return

    def _register(self, middleware: List[B]) -> Session:
        """
        Helper method that constructs a middleware_pipeline with the specified middleware
        """

        Logger.info("%s._register: method called", type(self))

        if middleware:
            middleware_pipeline = MiddlewarePipeline()
            for ware in middleware:
                middleware_pipeline.add_middleware(ware)

            self.session.mount(f"{self._protocol}://", middleware_pipeline)

        return self.session
