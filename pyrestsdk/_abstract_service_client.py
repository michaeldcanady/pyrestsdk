from typing import Optional, TypeVar
from abc import ABC, abstractmethod
from requests import Response, Session


S = TypeVar('S', bound='AbstractServiceClient')

class AbstractServiceClient(ABC):

    __instance: Optional[S] = None

    def __new__(cls, *args, **kwargs) -> S:
        if AbstractServiceClient.__instance is None:
            AbstractServiceClient.__instance = object.__new__(cls)
        return AbstractServiceClient.__instance

    @abstractmethod
    def get(self, url: str, **kwargs) -> Response: ...

    @abstractmethod
    def options(self, url: str, **kwargs) -> Response: ...

    @abstractmethod
    def post(self, url: str, data=None, json=None, **kwargs) -> Response: ...

    @abstractmethod
    def put(self, url: str, data=None, **kwargs) -> Response: ...

    @abstractmethod
    def patch(self, url: str, data=None, **kwargs) -> Response: ...

    @abstractmethod
    def delete(self, url: str, **kwargs) -> Response: ...

    @abstractmethod
    def _get_session(*args, **kwargs) -> Session: ...