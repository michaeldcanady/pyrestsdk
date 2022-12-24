from typing import TypeVar

# internal imports
from pyrestsdk.credential import AbstractCredential
from pyrestsdk.middleware._base_middleware import BaseMiddleware

C = TypeVar('C', bound=AbstractCredential)
A = TypeVar('A', bound='BaseAuthorizationHandler')

class BaseAuthorizationHandler(BaseMiddleware):

    credential: C
    retry_count: int = 0

    def __init__(self, credential: C, **kwargs):
        super().__init__()
        self.credential = credential
