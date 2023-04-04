"""Houses Query Option Type"""

from pyrestsdk.type.model._option import Option


class QueryOption(Option): #pylint: disable=too-few-public-methods
    """Query Option Type"""

    def __str__(self) -> str:

        return f"{self.name}={self.value}"
