"""Houses Supports Invoke Collection Request
"""

from typing import TypeVar, List

from abc import ABC

from pyrestsdk.type.model import Entity
from pyrestsdk.type.exception import UnexpectedReturnType
from pyrestsdk.request.supports_types._supports_base_invoke_request import SupportsBaseInvokeRequest

from pyrestsdk.type.enum import HttpsMethod

T = TypeVar("T", bound=Entity)
S = TypeVar("S", bound="SupportsInvokeCollectionRequest")

class SupportsInvokeCollectionRequest(SupportsBaseInvokeRequest[T], ABC):
    """Supports Invoke Request
    
    Request supports invokation at later time
    """

    @property
    def invoke_request(self:S) -> List[T]:
        """Invokes Request Expecting list of value return type

        Raises:
            UnexpectedReturnType: Error when return type is other than generic list

        Returns:
            List[T]: The list of value
        """

        _return = self.send_request(self.input_object)

        if self.request_method in [HttpsMethod.POST, HttpsMethod.PUT]:
            return _return

        if not isinstance(_return, list) or _return is None:
            raise UnexpectedReturnType(type(_return), List[self.generic_type])

        return _return
