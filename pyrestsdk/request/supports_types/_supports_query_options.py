"""Houses Supports Query Options"""

from pyrestsdk.type.model import QueryOptionCollection
from pyrestsdk.request.supports_types._supports_types import SupportTypes


class SupportsQueryOptions(SupportTypes):
    """Supports Query Options Type"""

    __slots__ = ()

    _query_options: QueryOptionCollection
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._query_options = QueryOptionCollection()

    @property
    def query_options(self) -> QueryOptionCollection:
        """Gets Query Options"""

        return self._query_options
