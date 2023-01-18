"""House Abstract Basic Credential"""

from abc import abstractmethod
from pyrestsdk.credential._abstract_credential import AbstractCredential


class AbstractBasicCredential(AbstractCredential):
    """Abstract Basic Credential Type"""

    @abstractmethod
    def get_basic(self, /) -> str:
        """Gets the basic credential encoded string"""
