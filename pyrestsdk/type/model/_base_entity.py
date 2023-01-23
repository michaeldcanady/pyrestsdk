"""Houses Base Entity"""

from __future__ import annotations
from typing import TYPE_CHECKING, Dict, TypeVar, Type
from abc import abstractmethod

if TYPE_CHECKING:
    from pyrestsdk import AbstractServiceClient

S = TypeVar("S", bound="BaseEntity")
A = TypeVar("A", bound="AbstractServiceClient")


class BaseEntity:
    """Base Entity Type"""
    
    __slots__ = ["__client"]
    
    __client: A

    def __init__(self: S, client: A) -> None:
        self.__client = client

    @property
    @abstractmethod
    def as_dict(self) -> Dict:
        """Gets the object as it's dict representation"""

    @property
    @abstractmethod
    def as_json(self) -> str:
        """Gest the object's json representation"""

    @property
    def Client(self: S) -> A:
        """Gets the client"""
        return self.__client

    @classmethod
    @abstractmethod
    def from_json(cls: Type[S], entry: Dict) -> S:
        """Converts Json to class type"""
