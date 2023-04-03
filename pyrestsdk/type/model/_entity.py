"""Houses Base Entity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from pyrestsdk.type.model._abstract_entity import AbstractEntity

from pyrestsdk import AbstractServiceClient

S = TypeVar("S", bound="Entity")
A = TypeVar("A", bound="AbstractServiceClient")


class Entity(AbstractEntity):
    """Base Entity Type"""

    _client: A

    def __init__(self: S, client: A) -> None:
        
        if not (isinstance(client, AbstractServiceClient) or issubclass(type(client), AbstractServiceClient)):
            raise TypeError(f"Expected an instance or subclass of AbstractServiceClient, but got {type(client)}")

        super().__init__(client)

        self._client = client

    @property
    def client(self: S) -> A:
        """Gets the client"""
        return self._client
