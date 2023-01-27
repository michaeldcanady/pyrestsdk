"""Houses Supports Query Options"""

from pyrestsdk.type.model import QueryOptionCollection


class SupportsQueryOptions:
    """Supports Query Options Type"""

    __slots__ = ["_query_options"]

    _query_options: QueryOptionCollection
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._query_options = QueryOptionCollection()

    @property
    def query_options(self) -> QueryOptionCollection:
        """Gets Query Options"""

        return self._query_options
