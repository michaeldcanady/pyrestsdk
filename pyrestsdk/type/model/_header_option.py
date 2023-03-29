"""Houses Header Option"""
from typing import Dict, Any

from pyrestsdk.type.model._option import Option


class HeaderOption(Option):
    """Header Option Type"""

    @property
    def as_dict(self) -> Dict[str, str]:
        return {str(self.name): str(self.value)}