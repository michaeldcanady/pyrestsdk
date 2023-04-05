"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from typing import Any

from urllib.parse import urlencode

from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._query_option import QueryOption

class QueryOptionCollection(OptionsCollection[QueryOption]):
    """
    Query Option Collection
    =======================
    
    """

    def __str__(self) -> str:

        return urlencode(self.as_dict)

    def add(self, key: str, value: Any) -> None:
        """Adds Query Option to collection

        Args:
            key (str): Name of query option
            value (Any): Value of query option
        """
        self.append(QueryOption(key, value))
