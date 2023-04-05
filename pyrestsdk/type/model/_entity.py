"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from __future__ import annotations

from typing import TypeVar

from pyrestsdk.type.model._abstract_entity import AbstractEntity

from pyrestsdk import ServiceClient

S = TypeVar("S", bound="Entity")
A = TypeVar("A", bound="ServiceClient")


class Entity(AbstractEntity):
    """
    Entity
    ======
    
    """

    _client: A

    def __init__(self: S, client: A) -> None:
        if not (
            isinstance(client, ServiceClient)
            or issubclass(type(client), ServiceClient)
        ):
            raise TypeError(
                f"Expected an instance or subclass of AbstractServiceClient, but got {type(client)}"
            )

        super().__init__(client)

        self._client = client

    @property
    def client(self: S) -> A:
        """Gets the client"""
        return self._client
