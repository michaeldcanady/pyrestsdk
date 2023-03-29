from typing import TypeVar

from pyrestsdk.type.model import Entity
from pyrestsdk.type.exception import UnexpectedReturnType
from pyrestsdk.request.supports_types._supports_base_invoke_request import SupportsBaseInvokeRequest

T = TypeVar("T", bound=Entity)
S = TypeVar("S", bound="SupportsInvokeRequest")

class SupportsInvokeRequest(SupportsBaseInvokeRequest):
    """Supports Invoke Request
    
    Request supports invokation at later time
    """

    @property
    def invoke_request(self:S) -> T:
        """Invokes Request Expecting single value return type

        Args:
            self (S): Supports Invoke Request Instance

        Raises:
            UnexpectedReturnType: Error when return type is other than generic

        Returns:
            T: The single value return
        """

        _return = self.Send(self.input_object)

        if not isinstance(_return, self.generic_type) or _return is None:
            raise UnexpectedReturnType(type(_return), type(self.generic_type))

        return _return
