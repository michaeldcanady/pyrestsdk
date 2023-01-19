from typing import TypeVar, List

from pyrestsdk.type.model import BaseEntity
from pyrestsdk.type.exception import UnexpectedReturnType
from pyrestsdk.request.supports_types._supports_base_invoke_request import SupportsBaseInvokeRequest

T = TypeVar("T", bound=BaseEntity)

class SupportsInvokeCollectionRequest(SupportsBaseInvokeRequest):

    @property
    def invoke_request(self) -> List[T]:

        _return = self.Send(self.input_object)

        if not isinstance(_return, list) or _return is None:
            raise UnexpectedReturnType(type(_return), List[self.generic_type])

        return _return