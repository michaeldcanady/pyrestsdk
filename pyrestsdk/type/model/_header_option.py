from typing import Any
# internal imports
from pyrestsdk.type.model._option import Option

class HeaderOption(Option):

    def __init__(self, name: str, value: Any) -> None:
        """Initalize new header option
        """
        
        super().__init__(name, value)