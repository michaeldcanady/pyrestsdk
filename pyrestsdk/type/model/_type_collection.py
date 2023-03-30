"""Houses Type Collection"""

from typing import MutableSequence, List, TypeVar, Iterator, Iterable

T = TypeVar("T")


class TypeCollection(MutableSequence[T]):
    """A collection type for storing elements with specific type constraints."""

    def __init__(self) -> None:
        """Initialize an empty TypeCollection.
        """

        self._internal_list: List[T] = []

    def __getitem__(self, index: int) -> T:
        """Get an item at the given index.

        Args:
            index (int): The index of the item

        Returns:
            T: The item
        """

        return self._internal_list[index]

    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the elements in the collection.

        Yields:
            Iterator[T]: The iterator over the elements in the collection.
        """
        
        return iter(self._internal_list)

    def __len__(self) -> int:
        """Return the number of elements in the collection.

        Returns:
            int: The number of elements in the collection.
        """

        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        """Delete an item at the given index.

        Args:
            index (int): The index
        """

        del self._internal_list[index]

    def __setitem__(self, index: int, value: T) -> None:
        """Set the value of an item at the given index.

        Args:
            index (int): The index
            value (T): The value
        """

        self._internal_list[index] = value

    def insert(self, index: int, value: T) -> None:
        """Insert an item at the given index.

        Args:
            index (int): The index
            value (T): The value
        """

        self._internal_list.insert(index, value)

    def __repr__(self) -> str:
        """Returns a string representation of the collection.

        Returns:
            str: A string representation of the collection.
        """

        return f"{type(self).__name__}({self._internal_list})"

    def append(self, value: T) -> None:
        """Append an item to the end of the collection.

        Args:
            value (T): Item to append
        """

        self._internal_list.append(value)

    def remove(self, value: T) -> None:
        """Remove the first occurrence of the given value from the collection.

        Args:
            value (T): The value to remove
        
        Raises:
            ValueError: if the value is not present.
        """

        self._internal_list.remove(value)

    def clear(self) -> None:
        """Clear all elements in the collection.
        """

        self._internal_list.clear()

    def count(self, value: T) -> int:
        """Returns the number of occurrences of the given value in the collection.

        Args:
            value (T): The value

        Returns:
            int: The number of occurrences of the given value in the collection.
        """

        return self._internal_list.count(value)

    def index(self, value: T, *args) -> int:
        """Return the first index of the given value in the collection.

        Args:
            value (T): The value
        
        Raises:
            ValueError: if the value is not present.

        Returns:
            int: The first index of the given value in the collection.
        """

        return self._internal_list.index(value, *args)

    def reverse(self) -> None:
        """Reverse the order of the elements in the collection.
        """

        self._internal_list.reverse()

    def sort(self, /, *args, **kwargs) -> None:
        """Sort the elements in the collection in ascending order.

        The sort is in-place (i.e. the collection itself is modified)
        and stable (i.e. the order of two equal elements is maintained).

        If a key function is given, apply it once to each list
        item and sort them, ascending or descending, according to their
        function values.

        The reverse flag can be set to sort in descending order.
        """
        self._internal_list.sort(*args, **kwargs)

    def extend(self, values: Iterable[T]) -> None:
        """Extend the collection by appending elements from the given iterable.

        Args:
            values (Iterable[T]): The iterable elements to append
        """

        self._internal_list.extend(values)
