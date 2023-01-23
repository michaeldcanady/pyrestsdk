"""Houses Supports Post Method"""

from typing import TypeVar

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types.methods._supports_methods import SupportsMethods
from pyrestsdk.type.model import BaseEntity

O = TypeVar("O", bound=BaseEntity)
S = TypeVar("S", bound="SupportsPostMethod")


class SupportsPostMethod(SupportsMethods):
    """Supports Post Method Type"""

    def Post(self: S, input_object: O) -> S:
        """Sets request to put request"""

        self._update_request_type(HttpsMethod.POST, input_object)

        return self
