from typing import Type, TypeVar, get_args

from pyrestsdk.request.supports_types._supports_types import SupportTypes

T = TypeVar("T")
B = TypeVar("B", bound="SupportsGenericType")

class SupportsGenericType(SupportTypes):

    

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

        # used if type arg is provided in constructor
        orig_value = getattr(self, "__orig_class__", None)

        if orig_value is None:
            # used if typ arg is provided when subclassing
            orig_bases = getattr(self, "__orig_bases__")
            # way to find generic with mixins
            orig_value = [base for base in orig_bases if getattr(base, "_typevar_types", False)][0]

        return get_args(orig_value)[0]