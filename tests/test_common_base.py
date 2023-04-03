import pytest
from pyrestsdk.type.model import CommonBase

class TestCommonBase(CommonBase):
    def __init__(self, arg1, arg2, kwarg1=None, kwarg2=None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.kwarg1 = kwarg1
        self.kwarg2 = kwarg2
        super().__init__()

def test_common_base_constructor():
    # Arrange
    arg1 = "test_arg1"
    arg2 = "test_arg2"
    kwarg1 = "test_kwarg1"
    kwarg2 = "test_kwarg2"

    # Act
    obj = TestCommonBase(arg1, arg2, kwarg1=kwarg1, kwarg2=kwarg2)

    # Assert
    assert obj.arg1 == arg1
    assert obj.arg2 == arg2
    assert obj.kwarg1 == kwarg1
    assert obj.kwarg2 == kwarg2

def test_common_base_set_attribute():
    # Arrange
    obj = TestCommonBase("test_arg1", "test_arg2")

    # Act/Assert
    with pytest.raises(AttributeError):
        obj.new_attr = "new_value"
