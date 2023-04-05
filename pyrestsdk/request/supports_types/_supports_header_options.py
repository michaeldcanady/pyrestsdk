"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk.type.model import HeaderOptionCollection
from pyrestsdk.request.supports_types._supports_types import SupportTypes


class SupportsHeaderOptions(SupportTypes): #pylint: disable=too-few-public-methods
    """
    Supports Header Options
    =======================
    
    
    """

    _header_options: HeaderOptionCollection

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._header_options = HeaderOptionCollection()

    @property
    def header_options(self) -> HeaderOptionCollection:
        """Gets the Header Options

        Returns:
            HeaderOptionCollection: The Header Options
        """

        return self._header_options
