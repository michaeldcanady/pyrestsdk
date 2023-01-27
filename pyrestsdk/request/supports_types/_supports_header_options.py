"""Houses Supports Header Options"""

from pyrestsdk.type.model import HeaderOptionCollection


class SupportsHeaderOptions:
    """Supports Header Options Type"""

    __slots__ = ["_header_options"]

    _header_options: HeaderOptionCollection
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._header_options = HeaderOptionCollection()

    @property
    def header_options(self) -> HeaderOptionCollection:
        """Gets Header Options"""

        return self._header_options
