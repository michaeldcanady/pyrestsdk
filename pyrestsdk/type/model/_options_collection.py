from typing import MutableSequence, List, Dict, TypeVar

# internal imports
from pyrestsdk.type.model._option import Option

O = TypeVar("O", bound=Option)

class OptionsCollection(MutableSequence[O]):
    def __init__(self) -> None:
        super().__init__()
        self._internal_list: List[O] = []

    def append(self, __option: O) -> None:
        self._internal_list.append(__option)

    def __getitem__(self, index: int) -> Option:
        return self._internal_list[index]

    def __len__(self) -> int:
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        del self._internal_list[index]

    def __setitem__(self, index: int, value: O) -> None:
        self._internal_list[index] = value

    def insert(self, index: int, value: O) -> None:
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

    def __iter__(self):
        for k, v in self.asDict().items():
            if type(v) == list:
                v = ",".join(v)
            yield k, v

    def __str__(self) -> str:
        """Gets the object as it's string representation"""

        _params = []

        for k, v in iter(self):
            _params.append("%s=%s" % (k, v))

        return "&".join(_params)
