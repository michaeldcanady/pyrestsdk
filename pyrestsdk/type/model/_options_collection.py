"""Houses Options Collection"""

from typing import List, Dict, TypeVar, Any, Tuple, Iterator
from pyrestsdk.type.model._type_collection import TypeCollection
from pyrestsdk.type.model._option import Option

O = TypeVar("O", bound=Option)


class OptionsCollection(TypeCollection[O]):
    """Option Collection Type"""

    @property
    def options(self) -> Tuple[O]:
        """Gets the options

        Returns:
            Tuple[O]: The options
        """

        return tuple(self._internal_list)

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

    @property
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object as it's dictionary representation

        Returns:
            Dict[str, Any]: Object's dictionary representation
        """

        return {option.name: option.value for option in self._internal_list}

    def as_list(self) -> List[O]:
        """Gets the object as it's list representation"""

        return self._internal_list
