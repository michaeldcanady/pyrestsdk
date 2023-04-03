"""Houses Option"""

from typing import Any
from dataclasses import dataclass, fields

@dataclass
class Option:
    """Option Type"""

    name: str
    value: Any

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if field.type == Any:
                return
            if not isinstance(value, field.type):
                raise ValueError(f'Expected {field.name!r} to be {field.type}, '
                                f'got {type(value)}')
