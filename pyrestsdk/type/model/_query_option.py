from typing import Any

# internal imports
from pyrestsdk.type.model._option import Option

class QueryOption(Option):

    def __init__(self, name: str, value: Any) -> None:
        """Initialize new query option
        """

        super().__init__(name, value)