"""
Get Generic Type Mixin
======================

"""

from typing import (
    TypeVar,
    Type,
    get_args,
    _GenericAlias
)
from types import GenericAlias #pylint: disable=no-name-in-module

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
        generic_type = self._search_for_generic_type(orig_value)

        if generic_type is None:
            raise TypeError(f"No generic type found in bases {orig_value}")

        return generic_type

    def _search_for_generic_type(self, orig_value: object):

        generic_type = None

        for base in orig_value:

            if isinstance(base, (GenericAlias, _GenericAlias)):
                generic_type = get_args(base)[0]
                break

            if (_or_value := getattr(base, "__orig_bases__", None)):
                return self._search_for_generic_type(_or_value)

        return generic_type
