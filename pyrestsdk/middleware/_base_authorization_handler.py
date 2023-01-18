"""Houses Base Authorization Handler"""

from typing import TypeVar
from pyrestsdk.credential import AbstractCredential
from pyrestsdk.middleware._base_middleware import BaseMiddleware

C = TypeVar("C", bound=AbstractCredential)
A = TypeVar("A", bound="BaseAuthorizationHandler")


class BaseAuthorizationHandler(BaseMiddleware):
    """Base Authorization Handler Type"""

    credential: C
    retry_count: int

    def __init__(self, credential: C, /):
        super().__init__()
        self.credential = credential
        self.retry_count = 0
