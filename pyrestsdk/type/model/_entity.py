"""Houses Base Entity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from pyrestsdk.type.model._abstract_entity import AbstractEntity

if TYPE_CHECKING:
    from pyrestsdk import AbstractServiceClient

S = TypeVar("S", bound="Entity")
A = TypeVar("A", bound="AbstractServiceClient")


class Entity(AbstractEntity):
    """Base Entity Type"""
    
    _client: A

    def __init__(self: S, client: A) -> None:
        self._client = client

    @property
    def Client(self: S) -> A:
        """Gets the client"""
        return self._client
