"""Houses Supports Header Options"""

from typing import Protocol
from pyrestsdk.type.model import HeaderOptionCollection


class SupportsHeaderOptions(Protocol):
    """Supports Header Options Type"""

    __slots__ = ["_header_options"]

    _header_options: HeaderOptionCollection

    @property
    def header_options(self) -> HeaderOptionCollection:
        """Gets Header Options"""

        return self._header_options
