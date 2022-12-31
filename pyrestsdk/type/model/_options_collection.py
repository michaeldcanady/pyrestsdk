from typing import MutableSequence, List, Dict, TypeVar, Iterator, Optional, Any, Tuple

# internal imports
from pyrestsdk.type.model._option import Option

O = TypeVar("O", bound=Option)

class OptionsCollection(MutableSequence[O]):
    def __init__(self) -> None:
        """Initalize new options collection
        """
        
        super().__init__()
        self._internal_list: List[O] = []

    def append(self, __option: O) -> None:
        """Adds object to end of collection
        """
        
        self._internal_list.append(__option)

    def __getitem__(self, index: int) -> Option:
        """Gets object at index
        """
        
        return self._internal_list[index]

    def __len__(self) -> int:
        """gets the length of the collection
        """
        
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        """Deletes object at index
        """
        
        del self._internal_list[index]

    def __setitem__(self, index: int, value: O) -> None:
        """Sets object at index
        """
        
        self._internal_list[index] = value

    def insert(self, index: int, value: O) -> None:
        """Insert object before index.
        """
        
        return self._internal_list.insert(index, value)

    def asDict(self) -> Dict:
        """Gets the object as it's dict representation
        """

        _return: Dict = {}

        for value in self._internal_list:
            _return.update(value.asDict())

        return _return

    def asList(self) -> List[O]:
        """Gets the object as it's list representation
        """

        return [_option for _option in self._internal_list]

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        """Get iterator of option name, value
        """
        
        for k, v in self.asDict().items():
            if type(v) == list:
                v = ",".join(v)
            yield k, v

    def __str__(self) -> str:
        """Gets string representation
        """

        _params = []

        for k, v in iter(self):
            _params.append("%s=%s" % (k, v))

        return "&".join(_params)
