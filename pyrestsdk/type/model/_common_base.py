from typing import Any, Callable
from functools import wraps
from sys import _getframe

def frozen(cls: Callable) -> Callable:
    """
    Decorator for freezing ability to set attributes outside of specific instances.
    """
    # Replace the class's __setattr__ method with the frozen version
    original_setattr = cls.__setattr__

    @wraps(cls.__setattr__)
    def setattr_frozen(self: Any, name: str, value: Any) -> None:
        co_name = _getframe(1).f_code.co_name

        # Checks if attribute already exists or if it is being set in __init__
        if not hasattr(self, name) and co_name != "__init__":
            raise AttributeError(f"You cannot add attributes to {self.__class__.__name__}")

        # Checks if attribute is a 'protected' attribute (begins with _) and is being set outside of __init__
        if name.startswith("_") and co_name != "__init__":
            raise AttributeError(f"You cannot set value of protected attribute {self.__class__.__name__}.{name}")

        # Calls the original __setattr__ function
        original_setattr(self, name, value)

    # Replace the class's __setattr__ with the frozen version
    setattr(cls, "__setattr__", setattr_frozen)
    return cls

@frozen
class CommonBase:
    """Common Base Type"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
