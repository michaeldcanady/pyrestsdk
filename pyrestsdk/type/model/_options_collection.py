from typing import MutableSequence, List, Iterator, Dict

# internal imports
from pyrestsdk.type.model._option import Option

class OptionsCollection(MutableSequence[Option]):

    _internal_list: List[Option] = []

    def __init__(self) -> None:
        super().__init__()
    
    def append(self, __option: Option) -> None:
        self._internal_list.append(__option)

    def __iter__(self) -> Iterator[Option]:
        for value in self._internal_list:
            yield value

    def __getitem__(self, index: int) -> Option:
        return self._internal_list[index]

    def __len__(self) -> int:
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        del self._internal_list[index]

    def __setitem__(self, index: int, value: Option) -> None:
        self._internal_list[index] = value
    
    def insert(self, index: int, value: Option) -> None:
        return self._internal_list.insert(index, value)

    def asDict(self) -> Dict:

        _return: Dict = {}

        for value in self._internal_list:
            _return.update(value.asDict())

        return _return

    def __str__(self) -> str:

        _params = []

        for k,v in self.asDict().items():
            if type(v) == list:
                v = ",".join(v)
            _params.append("%s=%s" % (k,v))
        
        return "&".join(_params)