"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk.type.model._option import Option


class QueryOption(Option): #pylint: disable=too-few-public-methods
    """
    Query Option
    ============
    
    """

    def __str__(self) -> str:

        return f"{self.name}={self.value}"
