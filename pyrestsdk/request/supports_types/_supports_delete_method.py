"""Houses Supports Delete Method"""

from sys import version_info

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types._supports_methods import SupportsMethods


class SupportsDeleteMethod(SupportsMethods):
    """Supports Delete Method Type"""

    @property
    def Delete(self) -> Self:
        """Sets request to delete request"""

        self._update_request_type(HttpsMethod.DELETE, None)

        return self
