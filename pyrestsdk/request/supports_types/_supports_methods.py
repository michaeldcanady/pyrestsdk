"""Houses Supports Methods"""

from typing import Protocol, Optional, TypeVar
from logging import getLogger

from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import BaseEntity

S = TypeVar("S", bound=BaseEntity)

Logger = getLogger(__name__)


class SupportsMethods(Protocol):
    """Supports Methods Type"""

    __slots__ = ["_method", "_input_object"]

    _method: HttpsMethod
    _input_object: Optional[S]

    @property
    def request_method(self) -> HttpsMethod:

        Logger.info("%s.request_method: function called", type(self).__name__)

        return self._method

    @request_method.setter
    def request_method(self, new_method: HttpsMethod) -> None:

        Logger.info("%s.request_method: function called", type(self).__name__)

        self._method = new_method

        Logger.debug(
            "%s.request_method Method set to %s", type(self).__name__, new_method
        )

    @property
    def input_object(self) -> Optional[S]:

        Logger.info("%s.input_object: function called", type(self).__name__)

        return self._input_object

    @input_object.setter
    def input_object(self, new_object: Optional[S]) -> None:

        Logger.info("%s.input_object: function called", type(self).__name__)

        self._input_object = new_object

        Logger.debug(
            "%s.input_object input object set to %s", type(self).__name__, new_object
        )

    def _update_request_type(
        self, method: HttpsMethod, input_object: Optional[S]
    ) -> None:
        """Updates the request type, sSets the method and object to the provided values"""

        Logger.info("%s._update_request_type: function called", type(self).__name__)

        self.request_method = method
        self.input_object = input_object
