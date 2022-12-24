from __future__ import annotations
from typing import TYPE_CHECKING, Dict, TypeVar, Type
from abc import abstractmethod

if TYPE_CHECKING:
    from pyrestsdk import AbstractServiceClient

S = TypeVar('S', bound='BaseEntity')
A = TypeVar('A', bound='AbstractServiceClient')


class BaseEntity(object):

    __client: A

    @property
    @abstractmethod
    def Json(self: S) -> Dict: ...

    @property
    @abstractmethod
    def Client(self: S) -> A: ...

    @classmethod
    @abstractmethod
    def fromJson(cls: Type[S], entry: Dict) -> S: ...