from typing import Any, Tuple, Dict, Any, Type


def frozen(set):
    """Raise an error when trying to set an undeclared name, or when calling
    from a method other than Frozen.__init__ or the __init__ method of
    a class derived from Frozen"""

    def set_attr(self, name: str, value: Any):
        from sys import _getframe

        co_name = _getframe(1).f_code.co_name
        instance_type = type(self)

        # checks if attribute already exists or if it is being set in __init__
        if (not hasattr(self, name)) and (co_name != "__init__"):
            raise AttributeError(
                f"You cannot add attributes to {instance_type.__name__}"
            )
        # cheks if attribute is a 'protected' (begins with _) and is being set outside of property or __init__
        elif (
            name.startswith("_")
            and (co_name != "__init__")
            and (
                co_name == "<module>"
                or (type(getattr(instance_type, co_name)) is not property)
            )
        ):
            raise AttributeError(
                f"You cannot set value of protected attribute {instance_type.__name__}.{name}"
            )

        if co_name == "__init__":
            for k, v in _getframe(1).f_locals.items():
                if k == "self" and isinstance(v, self.__class__):

                    return set(self, name, value)

        return set(self, name, value)

    return set_attr


class FrozenAttributes(type):
    """MetaClass for freezing ability to set attributes outside of specific instances"""

    def __new__(
        cls, __name: str, __bases: Tuple[Type, ...], __namespace: Dict[str, Any]
    ) -> "FrozenAttributes":
        obj = super().__new__(cls, __name, __bases, __namespace)
        obj.__setattr__ = frozen(object.__setattr__)  # type: ignore
        return obj


class CommonBase(metaclass=FrozenAttributes):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
