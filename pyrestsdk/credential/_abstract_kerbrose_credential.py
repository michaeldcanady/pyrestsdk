"""Houses Abstract Kerbrose Credential"""

from abc import abstractmethod
from pyrestsdk.credential._abstract_credential import AbstractCredential


class AbstractKerbroseCredential(AbstractCredential): #pylint: disable=too-few-public-methods
    """Abstract Kerbrose Credential Type"""

    @abstractmethod
    def get_principle(self, /) -> str:
        """Gets the principle information for authing"""
