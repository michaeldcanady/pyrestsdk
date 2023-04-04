"""Houses Header Option"""
from typing import Dict

from pyrestsdk.type.model._option import Option


class HeaderOption(Option):
    """Header Option Type"""

    @property
    def as_dict(self) -> Dict[str, str]:
        """Converts the Header Option to a dictionary

        Returns:
            Dict[str, str]: The dictionary representation
        """

        return {str(self.name): str(self.value)}

    def __str__(self) -> str:

        return f"{self.name}:{self.value}"
