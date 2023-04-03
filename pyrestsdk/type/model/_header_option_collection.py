"""Houses Header Option Collection"""
from typing import Optional, Dict

from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._header_option import HeaderOption


class HeaderOptionCollection(OptionsCollection[HeaderOption]):
    """Header Option Collection Type"""

    def __init__(self, headers: Optional[Dict[str, str]] = None) -> None:
        """Initializes a new Header Option Collection

        Args:
            headers (Optional[Dict[str, str]], optional):
            The headers to initialize the collection with. Defaults to None.
        """

        super().__init__()
        if headers is None:
            return None
        for key, value in headers.items():
            self.append(HeaderOption(key, value))
        return None

    def add(self, name: str, value: str) -> None: #pylint: disable=arguments-renamed
        """Adds a new header option

        Args:
            name (str): Header name
            value (str): Header value
        """
        self.append(HeaderOption(name=name, value=value))
