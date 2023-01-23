"""Houses Supports Put Method"""

from typing import TypeVar, Dict, Union, Any

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types.methods._supports_methods import SupportsMethods
from pyrestsdk.type.model import BaseEntity

O = TypeVar("O", bound=BaseEntity)
S = TypeVar("S", bound="SupportsPutMethod")


class SupportsPutMethod(SupportsMethods):
    """Supports Put Method Type"""

    def Put(self: S, input_object: Union[O, Dict[str, Any]]) -> S:
        """Sets request to put request"""

        self._update_request_type(HttpsMethod.PUT, input_object)

        return self
