"""Houses Header Option Collection"""

from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._header_option import HeaderOption


class HeaderOptionCollection(OptionsCollection[HeaderOption]):
    """Header Option Collection Type"""
    
    def __init__(self) -> None:
        super().__init__()
