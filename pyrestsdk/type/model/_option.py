from abc import ABC, abstractmethod
from typing import Dict

class Option(ABC):

    _name: str
    _value: str

    def __init__(self, name: str, value: str) -> None:
        super().__init__()
        self._name = name
        self._value = value

    @property
    def Name(self) -> str:
        return self._name
    
    @property
    def Value(self) -> str:
        return self._value

    def asDict(self) -> Dict:
        return {
            self.Name: self.Value
        }