# internal imports
from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._query_option import QueryOption

class QueryOptionCollection(OptionsCollection[QueryOption]):

    def __init__(self) -> None:
        super().__init__()