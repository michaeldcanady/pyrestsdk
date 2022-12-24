

# internal imports
from pyrestsdk.type.model._option import Option

class QueryOption(Option):

    def __init__(self, name: str, value: str) -> None:
        super().__init__(name, value)