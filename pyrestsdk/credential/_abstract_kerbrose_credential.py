from abc import abstractmethod

# internal imports
from pyrestsdk.credential._abstract_credential import AbstractCredential


class AbstractKerbroseCredential(AbstractCredential):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_principle(self) -> str:
        """Gets the principle information for authing
        """