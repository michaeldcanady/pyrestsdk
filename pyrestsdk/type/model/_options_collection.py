"""Houses Options Collection"""

from typing import (
    List,
    Dict,
    TypeVar,
    Any,
    Tuple,
    overload,
    Union,
    Iterable,
    Type,
    Optional,
)
from abc import abstractmethod

from pyrestsdk.type.model._type_collection import TypeCollection
from pyrestsdk.type.model._option import Option
from pyrestsdk.type.model._get_generic_type_mixin import GetGenericTypeMixin

O = TypeVar("O", bound=Option)
OC = TypeVar("OC", bound="OptionsCollection")


class OptionsCollection(GetGenericTypeMixin, TypeCollection[O]):
    """Option Collection Type"""

    element_type: Type[O]

    def __init__(
        self, options: Optional[Union[Iterable[O], Dict[str, Any]]] = None
    ) -> None:
        super().__init__()
        self.element_type = self._get_generic_type()

        if options is None:
            return

        if isinstance(options, dict):
            for key, value in options.items():
                self.add(key, value)
            return

        for option in options:
            self.append(option)

    @property
    def options(self) -> Tuple[O]:
        """Gets the options

        Returns:
            Tuple[O]: The options
        """

        return tuple(self._internal_list)

    def __getitem__(self, index: int) -> Option:
        """Gets object at index"""

        return self._internal_list[index]

    def __len__(self) -> int:
        """gets the length of the collection"""

        return len(self._internal_list)

    def __delitem__(self, index: int) -> None:
        """Deletes object at index"""

        del self._internal_list[index]

    def __setitem__(self, index: int, value: O) -> None:
        """Sets object at index"""

        self._internal_list[index] = value

    @overload
    def extend(self, new_options: Dict[str, Any]) -> None: #pylint: disable=arguments-renamed
        ...

    @overload
    def extend(self, new_options: Iterable[O]) -> None: #pylint: disable=arguments-renamed
        ...

    def extend(self, new_options: Union[Iterable[O], Dict[str, Any]]) -> None: #pylint: disable=arguments-renamed
        cleaned_new_options = []

        if isinstance(new_options, dict):
            for key, value in new_options.items():
                print(self.element_type)
                cleaned_new_options.append(self.element_type(key, value))
        else:
            cleaned_new_options = new_options

        return super().extend(cleaned_new_options)

    @property
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object as it's dictionary representation

        Returns:
            Dict[str, Any]: Object's dictionary representation
        """

        print(self._internal_list)

        return {option.name: option.value for option in self._internal_list}

    def as_list(self) -> List[O]:
        """Gets the object as it's list representation"""

        return self._internal_list

    def remove(self, option_name: str) -> None: #pylint: disable=arguments-renamed
        """Remove the option with the given name from the collection.

        Args:
            option_name (str): The name of the option to remove.

        Raises:
            ValueError: If the option with the given name is not present in the collection.
        """

        for i, option in enumerate(self._internal_list):
            if option.name == option_name:
                del self[i]
                return

        raise ValueError(f"Option '{option_name}' is not present in the collection.")

    def get(self, option_name: str, default: Any = None) -> Any:
        """Get the value of the HeaderOption with the specified name.

        Args:
            option_name (str): The name of the HeaderOption to get the value of.
            default (Any, optional): The default value to return if the HeaderOption is not found.

        Returns:
            Any: The value of the HeaderOption,
            or the default value if the HeaderOption is not found.
        """

        for option in self._internal_list:
            if option.name == option_name:
                return option.value

        return default

    def set(self, name: str, value: Any) -> None:
        """Set the value of an option with a given name.

        Args:
            name (str): The name of the option
            value (Any): The value to set
        """
        for option in self._internal_list:
            if option.name == name:
                option.value = value
                return

        _value = self.element_type(name, value)

        # If the option was not found, add it as a new option
        self.append(self.element_type(name, value))

    @abstractmethod
    def add(self, key: str, value: Any) -> None:
        """Adds new option to the collection

        Args:
            key (str): The key for the option
            value (Any): The value for the option
        """
