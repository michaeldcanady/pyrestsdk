"""Houses Type Collection"""

from typing import MutableSequence, List, Union, TypeVar, Iterator, Iterable

T = TypeVar("T")
OC = TypeVar("OC", bound="TypeCollection")


class TypeCollection(MutableSequence[T]):
    """Type Collection Type"""

    def __init__(self) -> None:
        super().__init__()

        self._internal_list: List[T] = []

    def __getitem__(self, index: int) -> T:
        return self._internal_list[index]

    def __iter__(self) -> Iterator[T]:
        for value in self._internal_list:
            yield value

    def __len__(self) -> int:
        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        del self._internal_list[index]

    def __setitem__(self, index: int, value: T) -> None:
        self._internal_list[index] = value

    def __lt__(self, other: List[T]) -> bool:
        return self._internal_list < other

    def __le__(self, other: List[T]) -> bool:
        return self._internal_list <= other

    def __eq__(self, other: List[T]) -> bool:
        return self._internal_list == other

    def __gt__(self, other: List[T]) -> bool:
        return self._internal_list > other

    def __ge__(self, other: List[T]) -> bool:
        return self._internal_list >= other

    def __contains__(self, item) -> bool:
        return item in self._internal_list

    def __copy__(self: OC) -> OC:
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__["_internal_list"] = self.__dict__["_internal_list"][:]
        return inst

    def append(self, __option: T) -> None:
        """Append object to the end of the list."""

        self._internal_list.append(__option)

    def insert(self, index: int, value: T) -> None:
        """Insert object before index."""
        self._internal_list.insert(index, value)

    def remove(self, value: T) -> None:
        """Remove first occurrence of value.

        Raises ValueError if the value is not present.
        """

        self._internal_list.remove(value)

    def clear(self) -> None:
        """Clears the collection"""
        self._internal_list.clear()

    def count(self, value: T) -> int:
        """Return number of occurrences of value."""

        return self._internal_list.count(value)

    def index(self, item, *args) -> int:
        """Return first index of value.

        Raises ValueError if the value is not present.
        """
        return self._internal_list.index(item, *args)

    def reverse(self) -> None:
        """Reverses the order of the collection"""

        self._internal_list.reverse()

    def sort(self, /, *args, **kwds):
        """Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified)
        and stable (i.e. the order of two equal elements is maintained).

        If a key function is given, apply it once to each list
        item and sort them, ascending or descending, according to their
        function values.

        The reverse flag can be set to sort in descending order.
        """
        self._internal_list.sort(*args, **kwds)

    def extend(self: OC, values: Union[Iterable, OC]) -> None:
        """Extend list by appending elements from the iterable."""

        if isinstance(values, TypeCollection) or issubclass(type(values), TypeCollection):
            other = iter(values)

        self._internal_list.extend(values)
