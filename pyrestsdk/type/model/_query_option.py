from typing import Dict, Iterable

# internal imports
from pyrestsdk.type.model._option import Option

class QueryOption(Option):

    def __init__(self, name: str, value: str) -> None:
        super().__init__(name, value)

    def __iter__(self) -> Iterable:
        return iter(self.asDict().items())

    def asDict(self) -> Dict:
        return {
            self.Name: self.Value
        }