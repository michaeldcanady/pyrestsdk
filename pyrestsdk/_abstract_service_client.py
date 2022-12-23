from typing import Optional
from abc import ABC, abstractmethod
from requests import Response, Session


class AbstractServiceClient(ABC):

    __instance: Optional['AbstractServiceClient'] = None

    def __new__(cls, *args, **kwargs):
        if not AbstractServiceClient.__instance:
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