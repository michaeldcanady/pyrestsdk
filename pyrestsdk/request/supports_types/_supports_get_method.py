"""Houses Supports Get Method"""

from sys import version_info

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types._supports_methods import SupportsMethods


class SupportsGetMethod(SupportsMethods):
    """Supports Get Method Type"""

    @property
    def Get(self) -> Self:
        """Sets request to get request"""

        self._update_request_type(HttpsMethod.GET, None)

        return self
