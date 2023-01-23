"""Houses Supports Delete Method"""

from typing import TypeVar

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types.methods._supports_methods import SupportsMethods

S = TypeVar("S", bound="SupportsDeleteMethod")


class SupportsDeleteMethod(SupportsMethods):
    """Supports Delete Method Type"""

    @property
    def Delete(self: S) -> S:
        """Sets request to delete request"""

        self._update_request_type(HttpsMethod.DELETE, None)

        return self
