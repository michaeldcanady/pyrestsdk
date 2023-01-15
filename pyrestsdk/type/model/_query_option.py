"""Houses Query Option Type"""

from typing import Any
from pyrestsdk.type.model._option import Option

class QueryOption(Option):
    """Query Option Type"""

    def __init__(self, name: str, value: Any) -> None:
        super().__init__(name, value)