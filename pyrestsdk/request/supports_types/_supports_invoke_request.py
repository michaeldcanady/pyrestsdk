from typing import TypeVar

from pyrestsdk.type.model import Entity
from pyrestsdk.type.exception import UnexpectedReturnType
from pyrestsdk.request.supports_types._supports_base_invoke_request import SupportsBaseInvokeRequest

T = TypeVar("T", bound=Entity)

class SupportsInvokeRequest(SupportsBaseInvokeRequest):

    @property
    def invoke_request(self) -> T:

        _return = self.Send(self.input_object)

        if not isinstance(_return, self.generic_type) or _return is None:
            raise UnexpectedReturnType(type(_return), type(self.generic_type))

        return _return