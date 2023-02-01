"""Houses Supports Default Middleware Type"""

from typing import List, TypeVar

from requests import Session

from abc import ABC, abstractmethod

from pyrestsdk.middleware import BaseMiddleware

B = TypeVar("B", bound=BaseMiddleware)


class SupportsDefaultMiddleware(ABC):
    """Supports Default Middleware Type"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _register(self, middleware: List[B]) -> None:
        ...

    @abstractmethod
    def create_with_default_middleware(self, /) -> Session:
        """Applies the default middleware chain to the HTTP Client"""
