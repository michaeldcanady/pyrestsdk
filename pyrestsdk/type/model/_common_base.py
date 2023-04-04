"""
Common Base
===========
The shared parent for all types, it's used to keep the
user from mutating the class outside of being inherited.
"""

from typing import Any, Callable
from functools import wraps
import inspect


def frozen(cls: Callable) -> Callable:
    """
    Decorator for freezing ability to set attributes outside of specific instances.
    """
    # Replace the class's __setattr__ method with the frozen version
    original_setattr = cls.__setattr__

    @wraps(cls.__setattr__)
    def setattr_frozen(self: Any, name: str, value: Any) -> None:
        caller = inspect.stack()[1]
        co_name = caller.function

        # Allow assignments at the module level and during __init__
        if co_name in ["<module>", "__init__"]:
            original_setattr(self, name, value)
            return

        # Prevent adding new attributes
        if not hasattr(self, name):
            raise AttributeError(
                f"You cannot add attributes to {self.__class__.__name__}"
            )

        if isinstance(getattr(self.__class__, co_name, None), property):
            original_setattr(self, name, value)
            return

        # Prevent setting value of protected attributes, except for property setters
        if name.startswith("_"):
            raise AttributeError(
                f"You cannot set value of protected attribute {self.__class__.__name__}.{name}"
            )

        # Calls the original __setattr__ function
        original_setattr(self, name, value)

    # Replace the class's __setattr__ with the frozen version
    setattr(cls, "__setattr__", setattr_frozen)
    return cls


@frozen
class CommonBase:  # pylint: disable=too-few-public-methods
    """Common Base Type"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
