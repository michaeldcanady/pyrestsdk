"""
Get Generic Type Mixin
======================

"""

from typing import (
    TypeVar,
    Type,
    get_args,
)
from types import GenericAlias

O = TypeVar("O")
OC = TypeVar("OC", bound="GetGenericTypeMixin")

class GetGenericTypeMixin: #pylint: disable=too-few-public-methods
    """
    Allows fetching of class provided generic type
    """

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

    def _get_generic_type(self: OC) -> Type[O]:
        """Sets the generic type attribute"""

        orig_value = getattr(self, "__orig_bases__", None)
        if orig_value is None:
            orig_value = (getattr(self, "__orig_class__"),)

        # Find generic with mixins
        generic_type = None
        for base in orig_value:
            if isinstance(base, GenericAlias):
                generic_type = get_args(base)[0]
                break

        if generic_type is None:
            raise TypeError(f"No generic type found in bases {orig_value}")

        return generic_type
