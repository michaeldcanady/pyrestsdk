"""
Tests for the Entity Type
=========================

"""

from typing import TYPE_CHECKING, Any

import pytest
from pyrestsdk.type.model._abstract_entity import AbstractEntity
from pyrestsdk.type.model import Entity

if TYPE_CHECKING:
    from pyrestsdk import AbstractServiceClient

class MockClient:
    """
    Mock Client for testing
    """
    pass

class MockEntity(Entity):
    """
    Mock Entity for testing
    """
    pass

def test_entity_initialization():
    """
    Tests Entity Initialization
    """

    client = MockClient()
    entity = MockEntity(client)

    assert isinstance(entity, AbstractEntity)
    assert entity.client == client

def test_entity_client_property():
    """
    Tests if client can be changed outside of the init method
    """

    client = MockClient()
    entity = MockEntity(client)

    assert entity.client == client

    new_client = MockClient()
    with pytest.raises(AttributeError):
        entity.client = new_client
    assert entity.client == client

@pytest.mark.parametrize("client", [None, 42, "client", [1, 2, 3], {"key": "value"}])
def test_invalid_entity_client_type(client: Any):
    """Tests invalid entity client types

    Args:
        client (typing.Any): The client to test
    """

    with pytest.raises(TypeError):
        MockEntity(client)
