"""Houses Query Option Collection"""

from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._query_option import QueryOption
from urllib.parse import urlencode

class QueryOptionCollection(OptionsCollection[QueryOption]):
    """Query Option Collection Type"""

    def __str__(self) -> str:
        
        return urlencode(self.as_dict())