"""Houses Supports Header Options"""

from pyrestsdk.type.model import HeaderOptionCollection
from pyrestsdk.request.supports_types._supports_types import SupportTypes


class SupportsHeaderOptions(SupportTypes):
    """Supports Header Options Type"""

    

    _header_options: HeaderOptionCollection
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._header_options = HeaderOptionCollection()

    @property
    def header_options(self) -> HeaderOptionCollection:
        """Gets Header Options"""

        return self._header_options
