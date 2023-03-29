"""Houses Supports Post Method"""

from typing import TypeVar, Union, Dict, Any

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.request.supports_types.methods._supports_methods import SupportsMethods
from pyrestsdk.type.model import Entity

O = TypeVar("O", bound=Entity)
S = TypeVar("S", bound="SupportsPostMethod")


class SupportsPostMethod(SupportsMethods):
    """Supports Post Method Type"""

    def post(self: S, input_object: Union[O, Dict[str, Any]]) -> S:
        """Sets request to put request"""

        self._update_request_type(HttpsMethod.POST, input_object)

        return self
