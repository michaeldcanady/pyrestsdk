from abc import abstractmethod

# internal imports
from pyrestsdk.credential._abstract_credential import AbstractCredential

class AbstractBasicCredential(AbstractCredential):
    """The base for Basic Credentials
    """

    @abstractmethod
    def get_basic(self, *args, **kwargs) -> str: ...