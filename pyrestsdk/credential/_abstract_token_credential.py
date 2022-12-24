from abc import abstractmethod
from typing import TypeVar

# internal imports
from pyrestsdk.credential._abstract_credential import AbstractCredential
from pyrestsdk.type.model.token import AccessToken

A = TypeVar('A', bound=AccessToken)

class AbstractTokenCredential(AbstractCredential):
    """The base for token credentials
    """

    @abstractmethod
    def get_token(self, *args, **kwargs) -> A: ...