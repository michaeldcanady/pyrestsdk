"""Houses Supports Generic Type
"""

from typing import Type, TypeVar, get_args, Generic, _GenericAlias

from pyrestsdk.request.supports_types._supports_types import SupportTypes

T = TypeVar("T")
B = TypeVar("B", bound="SupportsGenericType")

class SupportsGenericType(SupportTypes, Generic[T]):
    """Supports Generic Type
    """

    _generic_type: Type[T]

    def __init__(self: B, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._generic_type = self._get_generic_type()

    @property
    def generic_type(self: B) -> Type[T]:
        """Gets the generic type"""

        return self._generic_type

    def _get_generic_type(self: B) -> Type[T]:
        """Sets the generic type attribute"""

        orig_value = getattr(self, "__orig_bases__", None)
        if orig_value is None:
            orig_value = (getattr(self, "__orig_class__"),)

        # Find generic with mixins
        generic_type = None
        for base in orig_value:
            if isinstance(base, _GenericAlias):
                generic_type = get_args(base)[0]
                break

        if generic_type is None:
            raise TypeError(f"No generic type found in bases {orig_value}")

        return generic_type
