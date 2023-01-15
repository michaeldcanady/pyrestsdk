"""Houses Option"""

from typing import Dict, Any, Iterable

class Option(object):
    """Object Type"""

    _name: str
    _value: Any

    def __init__(self, name: str, value: Any) -> None:
        super().__init__()
        self._name = name
        self._value = value

    @property
    def Name(self) -> str:
        """Gets/Sets the name of the option
        """

        return self._name

    @Name.setter
    def Name(self, name: str) -> None:
        self._name = name
    
    @property
    def Value(self) -> str:
        """Gets/Sets the value of the option
        """

        return self._value
    
    @Value.setter
    def Value(self, value: Any) -> None:
        
        self._value = value

    def asDict(self) -> Dict[str, Any]:
        """Gets the object as it's dict representation
        """

        return {
            self.Name: self.Value
        }

    def __iter__(self) -> Iterable:
        return iter(self.asDict().items())