"""Houses Client Factory"""
from typing import TypeVar, List
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
    
    def __init__(self, /, session: Session) -> None:
        super().__init__(session)
    
    def create_with_custom_middleware(self, middleware: List[B]) -> Session:
        
        if not middleware:
            raise ValueError("Please provide a list of custom middleware")
        self._register(middleware)
        return self.session
    
    def create_with_default_middleware(self, credential: C) -> Session:
        return Session()
    
    def _set_base_url(self, url: str) -> None:
        return
    
    def _register(self, middleware: List[B]) -> None:
        """
        Helper method that constructs a middleware_pipeline with the specified middleware
        """

        Logger.info("%s._register: method called", type(self))

        if middleware:
            middleware_pipeline = MiddlewarePipeline()
            for ware in middleware:
                middleware_pipeline.add_middleware(ware)

            self.session.mount("https://", middleware_pipeline)