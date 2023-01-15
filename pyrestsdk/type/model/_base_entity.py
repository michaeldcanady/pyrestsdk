"""Houses Base Entity"""

from __future__ import annotations
from typing import TYPE_CHECKING, Dict, TypeVar, Type
from abc import abstractmethod

if TYPE_CHECKING:
    from pyrestsdk import AbstractServiceClient

S = TypeVar('S', bound='BaseEntity')
A = TypeVar('A', bound='AbstractServiceClient')


class BaseEntity(object):
    """Base Entity Type"""

    def __init__(self, client: A) -> None:
        self.__client: A = client

    @property
    @abstractmethod
    def Json(self: S) -> Dict:
        """Gets the object as it's dict representation
        """

    @property
    @abstractmethod
    def asDict(self) -> Dict:
        """Gets the object as it's dict representation
        """
    
    @property
    @abstractmethod
    def __json__(self) -> str:
        """Gest the object's json representation
        """

    @property
    def Client(self: S) -> A:
        """Gets the client
        """
        return self.__client

    @classmethod
    @abstractmethod
    def fromJson(cls: Type[S], entry: Dict) -> S: ...