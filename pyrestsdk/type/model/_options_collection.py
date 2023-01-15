"""Houses Options Collection"""

from typing import List, Dict, TypeVar, Any
from pyrestsdk.type.model._type_collection import TypeCollection
from pyrestsdk.type.model._option import Option

O = TypeVar("O", bound=Option)

class OptionsCollection(TypeCollection[O]):
    """Option Collection Type"""

    def __getitem__(self, index: int) -> Option:
        return self._internal_list[index]

    def __len__(self) -> int:
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        del self._internal_list[index]

    def __setitem__(self, index: int, value: O) -> None:
        self._internal_list[index] = value

    def asDict(self) -> Dict[str, Any]:
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