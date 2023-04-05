"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from typing import List, TypeVar

from abc import ABC, abstractmethod

from requests import Session

from pyrestsdk.middleware import BaseMiddleware

B = TypeVar("B", bound=BaseMiddleware)


class SupportsDefaultMiddleware(ABC): #pylint: disable=too-few-public-methods
    """
    Supports Default Middleware
    ===========================
    
    This abstract base class is used to define an interface
    for HTTP Clients that support registering and using default
    middleware. Any class that extends this class is expected to
    implement the _register and create_with_default_middleware
    methods.

    Usage::
        # extend this class to create your HTTP Client
        class MyHttpClient(SupportsDefaultMiddleware):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)

            def _register(self, middleware: List[B]) -> None:
                # implementation details

            def create_with_default_middleware(self) -> Session:
                # implementation details
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def _register(self, middleware: List[B]) -> None:
        """register middleware"""

    @abstractmethod
    def create_with_default_middleware(self, /) -> Session:
        """Applies the default middleware chain to the HTTP Client"""
