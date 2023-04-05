"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from typing import Type, TypeVar, Generic

from pyrestsdk.request.supports_types._supports_types import SupportTypes
from pyrestsdk.type.model._get_generic_type_mixin import GetGenericTypeMixin

ENTITYTYPE = TypeVar("ENTITYTYPE")
BOUNDTYPE = TypeVar("BOUNDTYPE", bound="SupportsGenericType")

class SupportsGenericType(SupportTypes, GetGenericTypeMixin, Generic[ENTITYTYPE]): #pylint: disable=too-few-public-methods
    """
    Supports Generic Type
    =====================
    
    
    """

    _generic_type: Type[ENTITYTYPE]

    def __init__(self: BOUNDTYPE, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._generic_type = self._get_generic_type()

    @property
    def generic_type(self: BOUNDTYPE) -> Type[ENTITYTYPE]:
        """Gets the generic type"""

        return self._generic_type
