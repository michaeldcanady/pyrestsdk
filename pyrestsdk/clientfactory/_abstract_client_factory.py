"""Houses Abstract HTTP Client Factory"""
from typing import TypeVar, List
from logging import getLogger
from abc import ABC, abstractmethod
from requests import Session
from pyrestsdk.middleware import BaseMiddleware
from pyrestsdk.credential import AbstractBasicCredential

Logger = getLogger(__name__)

B = TypeVar("B", bound=BaseMiddleware)
C = TypeVar("C", bound=AbstractBasicCredential)


class AbstractHTTPClientFactory(ABC): #pylint: disable=too-few-public-methods
    """Abstract HTTP Client Factory Type"""

    session: Session

    def __init__(self, /, session: Session) -> None:
        self.session = session

    @abstractmethod
    def create_with_custom_middleware(self, middleware: List[B]) -> Session:
        """Applies the custom middleware chain to the HTTP Client

        Args:
            middleware (List[B]): List of middleware to register

        Returns:
            Session: The session with the implemented middleware
        """

        raise NotImplementedError("create_with_custom_middleware is not implemented")

    @abstractmethod
    def _set_base_url(self, url: str) -> None:
        """Helper method to set the base url

        Args:
            url (str): The URL to set the base URL to
        """

        raise NotImplementedError("_set_base_url is not implemented")

    @abstractmethod
    def _register(self, middleware: List[B]) -> None:
        """Helper method that constructs a middleware_pipeline with the specified middleware

        Args:
            middleware (List[B]): List of middleware to register
        """

        raise NotImplementedError("_register is not implemented")
