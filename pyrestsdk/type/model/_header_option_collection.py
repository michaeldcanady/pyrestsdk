
# internal imports
from pyrestsdk.type.model._options_collection import OptionsCollection
from pyrestsdk.type.model._header_option import HeaderOption

class HeaderOptionCollection(OptionsCollection[HeaderOption]):

    def __init__(self) -> None:
        """Initalize new header option collection
        """
        
        super().__init__()