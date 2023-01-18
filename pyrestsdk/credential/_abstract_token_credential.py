"""Houses the Abstract Token Credential"""

from abc import abstractmethod
from typing import TypeVar
from pyrestsdk.credential._abstract_credential import AbstractCredential
from pyrestsdk.type.model.token import AccessToken

A = TypeVar("A", bound=AccessToken)


class AbstractTokenCredential(AbstractCredential):
    """Abstract Token Credential Type"""

    @abstractmethod
    def get_token(self, /) -> A:
        """Gets the access token"""
