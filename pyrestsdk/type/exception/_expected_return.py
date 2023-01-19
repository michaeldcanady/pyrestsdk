"""Houses unexpected return"""

from typing import Type, TypeVar

R = TypeVar("R")
E = TypeVar("E")


class UnexpectedReturnType(Exception):
    """Unexpected Return Type"""
    
    def __init__(self, return_type: Type[R], expected_type: Type[E]) -> None:
        super().__init__(
            f"Unexpected return type: {return_type}, expected {expected_type}"
        )
