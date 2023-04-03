"""
Header Option Collection tests
==============================

Tests the HeaderOptionCollection
"""

from pyrestsdk.type.model import HeaderOptionCollection


def test_header_collection_create():
    """Test creating a header collection from a dictionary of options"""
    # Arrange
    header_dict = {"Content-Type": "application/json"}

    # Act
    header_collection = HeaderOptionCollection(header_dict)

    # Assert
    assert header_collection.as_dict == header_dict


def test_header_collection_create_empty():
    """Test creating an empty header collection"""
    # Arrange
    header_dict = {}

    # Act
    header_collection = HeaderOptionCollection(header_dict)

    # Assert
    assert header_collection.as_dict == header_dict


def test_header_collection_add():
    """Test adding an option to a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    header_collection.add("Authorization", "Bearer token")

    # Assert
    assert header_collection.as_dict == {
        "Content-Type": "application/json",
        "Authorization": "Bearer token",
    }


def test_header_collection_remove():
    """Test removing an option from a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json", "Authorization": "Bearer token"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    header_collection.remove("Authorization")

    # Assert
    assert header_collection.as_dict == {"Content-Type": "application/json"}


def test_header_collection_clear():
    """Test clearing a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json", "Authorization": "Bearer token"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    header_collection.clear()

    # Assert
    assert header_collection.as_dict == {}


def test_header_collection_get():
    """Test getting an option value from a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json", "Authorization": "Bearer token"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    content_type = header_collection.get("Content-Type")

    # Assert
    assert content_type == "application/json"


def test_header_collection_set():
    """Test setting an option value in a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json", "Authorization": "Bearer token"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    header_collection.set("Content-Type", "text/html")

    # Assert
    assert header_collection.as_dict == {
        "Content-Type": "text/html",
        "Authorization": "Bearer token",
    }


def test_header_collection_contains_true():
    """Test checking if an option is present in a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json", "Authorization": "Bearer token"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    contains = "Authorization" in header_collection.as_dict

    # Assert
    assert contains is True


def test_header_collection_contains_false():
    """Test checking if an option is not present in a header collection"""
    # Arrange
    header_dict = {"Content-Type": "application/json", "Authorization": "Bearer token"}
    header_collection = HeaderOptionCollection(header_dict)

    # Act
    contains = "Accept" in header_collection

    # Assert
    assert contains is False
