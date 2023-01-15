"""Houses Query Option Collection"""

from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._query_option import QueryOption

class QueryOptionCollection(OptionsCollection[QueryOption]):
    """Query Option Collection Type"""

    def __init__(self) -> None:
        super().__init__()