"""
Test Options Collection
=======================

Tests to validate OptionsCollections work as intended
"""

from typing import Any

from pyrestsdk.type.model import Option, OptionsCollection

class TestOption(Option):
    """
    Test Option
    """

class TestOptionsCollection(OptionsCollection[TestOption]):
    """
    Test Options Collection
    """

    def add(self, key: str, value: Any) -> None:
        self.append(TestOption(key, value))

def test_options_collection_create():
    """
    Tests creation of an OptionsCollection.
    """
    # Arrange
    options_dict = {"key1": "value1", "key2": "value2"}
    options_list = [TestOption("key1", "value1"), TestOption("key2", "value2")]

    # Act
    options_collection_1 = TestOptionsCollection(options_dict)
    options_collection_2 = TestOptionsCollection(options_list)

    # Assert
    assert options_collection_1.as_dict == options_dict
    assert options_collection_2.as_dict == options_dict

def test_options_collection_append():
    """
    Tests adding an option to an OptionsCollection.
    """
    # Arrange
    options_dict = {"key1": "value1"}
    options_collection = TestOptionsCollection(options_dict)

    # Act
    options_collection.append(TestOption("key2", "value2"))

    # Assert
    assert options_collection.as_dict == {"key1": "value1", "key2": "value2"}

def test_options_collection_clear():
    """
    Tests clearing an OptionsCollection.
    """
    # Arrange
    options_dict = {"key1": "value1", "key2": "value2"}
    options_collection = TestOptionsCollection(options_dict)

    # Act
    options_collection.clear()

    # Assert
    assert options_collection.as_dict == {}

def test_options_collection_extend_dict():
    """
    Tests extending an OptionsCollection with a dictionary.
    """
    # Arrange
    options_dict = {"key1": "value1"}
    options_collection = TestOptionsCollection()

    # Act
    options_collection.extend(options_dict)

    # Assert
    assert options_collection.as_dict == options_dict

def test_options_collection_extend_list():
    """
    Tests extending an OptionsCollection with a list.
    """
    # Arrange
    options_dict = {"key1": "value1", "key2": "value2"}
    options_list = [TestOption("key1", "new_value1"), TestOption("key3", "value3")]
    expected_options_dict = {"key1": "new_value1", "key2": "value2", "key3": "value3"}
    options_collection = TestOptionsCollection(options_dict)

    # Act
    options_collection.extend(options_list)

    # Assert
    assert options_collection.as_dict == expected_options_dict

def test_options_collection_remove():
    """
    Tests removing an option from an OptionsCollection.
    """
    # Arrange
    options_dict = {"key1": "value1", "key2": "value2"}
    expected_options_dict = {"key1": "value1"}
    options_collection = TestOptionsCollection(options_dict)

    # Act
    options_collection.remove("key2")

    # Assert
    assert options_collection.as_dict == expected_options_dict

def test_options_collection_get():
    # Arrange
    options_dict = {"key1": "value1", "key2": "value2"}
    options_collection = TestOptionsCollection(options_dict)

    # Act
    value = options_collection.get("key1")

    # Assert
    assert value == "value1"

    print(options_collection.as_dict)
    # Output: {'key1': 'value1', 'key2': 'value2'}

def test_options_collection_set():
    # Arrange
    options_dict = {"key1": "value1", "key2": "value2"}
    expected_options_dict = {"key1": "new_value1", "key2": "value2"}
    options_collection = TestOptionsCollection(options_dict)

    # Act
    options_collection.set("key1", "new_value1")

    # Assert
    assert options_collection.as_dict == expected_options_dict

    print(options_collection.as_dict)
    # Output: {'key1': 'new_value1', 'key2': 'value2'}

