"""Houses Option"""

from typing import Dict, Any
from dataclasses import dataclass
from json import dumps

@dataclass
class Option:
    """Option Type"""

    name: str
    value: Any

    @property
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object as it's dict representation"""

        return {self.name: self.value}

    def to_json(self) -> str:
        """Gets the ojbect as it's JSON representation"""

        return dumps(self.as_dict)
