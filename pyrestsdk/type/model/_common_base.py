"""Houses Common Base
"""

from typing import Any, Callable

from functools import wraps
from sys import _getframe

# https://code.activestate.com/recipes/252158/
def frozen(func: Callable[[Any, str, Any], Any]):
    """Raise an error when trying to set an undeclared name, or when calling
    from a method other than Frozen.__init__ or the __init__ method of
    a class derived from Frozen"""

    @wraps(func)
    def set_attr(self: Any, name: str, value: Any) -> None:

        co_name = _getframe(1).f_code.co_name

        allowed_methods = ["__init_subclass__", "__init__"]

        # checks if attribute already exists or if it is being set in __init__
        if (not hasattr(self, name)) and (co_name not in allowed_methods):
            raise AttributeError(
                f"You cannot add attributes to {self.__name__}"
            )
        # cheks if attribute is a 'protected' (begins with _)
        # and is being set outside of property or __init__
        elif (
            name.startswith("_")
            and (co_name not in allowed_methods)
            and (
                co_name == "<module>"
                or (not isinstance(getattr(self, co_name), property))
            )
        ):
            raise AttributeError(
                f"You cannot set value of protected attribute {self.__name__}.{name}"
            )

        if co_name == "__init__":
            for key, value in _getframe(1).f_locals.items():
                if key == "self" and isinstance(value, self.__class__):

                    func(self, name, value)

                    return None

        func(self, name, value)

        return None

    return set_attr


class FrozenAttributes(type):
    """MetaClass for freezing ability to set attributes outside of specific instances"""

    @frozen
    def __setattr__(cls, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)

class CommonBase():
    """Common Base Type"""

    __metaclass__ = FrozenAttributes

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
