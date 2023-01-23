"""Houses Supports Get Method"""

from typing import TypeVar

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types.methods._supports_methods import SupportsMethods

S = TypeVar("S", bound="SupportsGetMethod")


class SupportsGetMethod(SupportsMethods):
    """Supports Get Method Type"""

    @property
    def Get(self: S) -> S:
        """Sets request to get request"""

        self._update_request_type(HttpsMethod.GET, None)

        return self
