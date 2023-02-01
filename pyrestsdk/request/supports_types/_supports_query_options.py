"""Houses Supports Query Options"""

from pyrestsdk.type.model import QueryOptionCollection
from pyrestsdk.request.supports_types._supports_types import SupportTypes
from pyrestsdk.type.model import QueryOption

class SupportsQueryOptions(SupportTypes):
    """Supports Query Options Type"""

    _query_options: QueryOptionCollection
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._query_options = QueryOptionCollection()

    @property
    def query_options(self) -> QueryOptionCollection:
        """Gets Query Options"""

        return self._query_options

    def _split_query_options(self, query_string: str) -> None:
        """Parses query options from query string"""
        
        for option in query_string.split("&"):
            query_parameter, value = option.split("=")
            _query_parameter = QueryOption(query_parameter, value)
            self.query_options.append(_query_parameter)