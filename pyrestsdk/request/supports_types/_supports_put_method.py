"""Houses Supports Put Method"""

from sys import version_info
from typing import TypeVar

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types._supports_methods import SupportsMethods
from pyrestsdk.type.model import BaseEntity

S = TypeVar("S", bound=BaseEntity)


class SupportsPutMethod(SupportsMethods):
    """Supports Put Method Type"""

    def Put(self, input_object: S) -> Self:
        """Sets request to put request"""

        self._update_request_type(HttpsMethod.PUT, input_object)

        return self
