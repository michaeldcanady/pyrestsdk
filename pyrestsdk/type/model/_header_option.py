"""Houses Header Option"""

from typing import Any
from pyrestsdk.type.model._option import Option

class HeaderOption(Option):
    """Header Option Type"""

    def __init__(self, name: str, value: Any) -> None:
        super().__init__(name, value)