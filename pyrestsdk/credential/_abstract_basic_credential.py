"""House Abstract Basic Credential"""

from typing import Union

from abc import abstractmethod
from pyrestsdk.credential._abstract_credential import AbstractCredential


class AbstractBasicCredential(AbstractCredential):
    """Abstract Basic Credential Type"""

    @abstractmethod
    def __init__(self, username: str, password: str) -> None:
        """Instatiates new Basic Credential"""
        
        self.username = username
        self.password = password

    @abstractmethod
    def get_basic(self, /) -> str:
        """Gets the basic credential encoded string"""

    @abstractmethod
    def to_native_string(self, string: Union[str, bytes], encoding="ascii") -> str:
        """Given a string object, regardless of type, returns a representation of
        that string in the native string type, encoding and decoding where
        necessary. This assumes ASCII unless told otherwise.
        """