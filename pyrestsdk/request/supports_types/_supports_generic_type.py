"""Houses Supports Generic Type
"""

from typing import Type, TypeVar, Generic

from pyrestsdk.request.supports_types._supports_types import SupportTypes
from pyrestsdk.type.model._get_generic_type_mixin import GetGenericTypeMixin

T = TypeVar("T")
B = TypeVar("B", bound="SupportsGenericType")

class SupportsGenericType(SupportTypes, GetGenericTypeMixin, Generic[T]): #pylint: disable=too-few-public-methods
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
