"""
Authorization Handler
=====================
The base for all Authorization Handlers
"""

from typing import Optional, TypeVar, Union, Tuple, Mapping
from requests import PreparedRequest, Response
from pyrestsdk.middleware.authorizationhandler._base_authorization_handler import BaseAuthorizationHandler
from pyrestsdk.credential import AbstractCredential
from pyrestsdk.type.enum import FeatureUsageFlag

T = TypeVar("T", bound=AbstractCredential)
A = TypeVar("A", bound="AuthorizationHandler")

class AuthorizationHandler(BaseAuthorizationHandler):
    """Common Authorization Handler Type"""

    credential: T

    def __init__(self, credential: T, **kwargs) -> None:
        super().__init__(credential, **kwargs)

    def send(  # pylint: disable=too-many-arguments
        self: A,
        request: PreparedRequest,
        stream: bool = False,
        timeout: Optional[Union[float, Tuple[float, float], Tuple[float, None]]] = None,
        verify: bool = True,
        cert: Optional[
            Union[bytes, str, Tuple[Union[bytes, str], Union[bytes, str]]]
        ] = None,
        proxies: Optional[Mapping[str, str]] = None,
    ) -> Response:
        """Makes a network request if next is none, otherwise requests the next middleware to do

        Args:
            request (PreparedRequest): The network request

        Returns:
            Response: Response from network request
        """

        context = request.context  # type: ignore

        request.headers.update({"Authorization": self._get_auth_header()})

        context.set_feature_usage = FeatureUsageFlag.AUTH_HANDLER_ENABLED
        response = super().send(request, stream, timeout, verify, cert, proxies)

        # Token might have expired just before transmission, retry the request one more time
        if response.status_code == 401 and self.retry_count < 2:
            self.retry_count += 1
            return self.send(request, stream, timeout, verify, cert, proxies)
        return response

    def _get_auth_header(self: A) -> str:
        raise NotImplementedError("Subclasses must implement _get_auth_header method")
