"""Houses Option"""

from typing import Dict, Any, Iterable
from dataclasses import dataclass

@dataclass
class Option:
    """Object Type"""
    
    Name: str
    Value: Any
    
    def as_dict(self) -> Dict[str, Any]:
        """Gets the object as it's dict representation"""

        return {self.Name: self.Value}

    #def __iter__(self) -> Iterable:
    #    return iter(self.as_dict().items())
