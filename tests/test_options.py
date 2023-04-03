"""
Test Options
============
"""

import pytest
from pyrestsdk.type.model import Option

def test_option_construction():
    """Test Basic string construction of Option
    """

    test_option = Option("key1", "value1")

    assert test_option.name == "key1"
    assert test_option.value == "value1"

def test_invalid_option_construction():
    """Tests Invalid Option Construction
    """

    with pytest.raises(ValueError):
        Option(1,"value1")
