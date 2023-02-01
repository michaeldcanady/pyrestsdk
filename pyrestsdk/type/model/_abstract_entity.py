"""Houses Abstract Entity Type"""

from typing import Dict, Any, TypeVar, Type, TYPE_CHECKING

from abc import ABC, abstractmethod

from pyrestsdk.type.model._common_base import FrozenAttributes

if TYPE_CHECKING:
    from pyrestsdk import AbstractServiceClient

S = TypeVar("S", bound="AbstractEntity")
A = TypeVar("A", bound="AbstractServiceClient")

class AbstractEntity(metaclass=FrozenAttributes):
    """Abstract Entity Type"""
    
    _client: A

    @abstractmethod
    def __init__(self: S, client: A) -> None:
        """Instatiates new class"""
    
    @property
    @abstractmethod
    def Client(self: S) -> A:
        """Gets the client"""
    
    @property
    @abstractmethod
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object as it's dict representation"""

    @property
    @abstractmethod
    def as_json(self) -> str:
        """Gets the object's json representation"""
        
    @classmethod
    @abstractmethod
    def from_json(cls: Type[S], entry: Dict) -> S:
        """Converts Json to class type"""