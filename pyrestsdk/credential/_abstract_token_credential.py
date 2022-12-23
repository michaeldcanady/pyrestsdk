from abc import abstractmethod
from typing import Tuple, Any

# internal imports
from ._abstract_credential import AbstractCredential


class AbstractTokenCredential(AbstractCredential):
    """The base for token credentials
    """

    @abstractmethod
    def get_token(self, *args, **kwargs) -> Tuple[str, Any]: ...