"""Houses Option"""

from typing import Dict, Any
from dataclasses import dataclass
from json import dumps

@dataclass
class Option:
    """Option Type"""
    
    Name: str
    Value: Any
    
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object as it's dict representation"""

        return {self.Name: self.Value}

    def to_json(self) -> str:
        """Gets the ojbect as it's JSON representation"""
        
        return dumps(self.as_dict)