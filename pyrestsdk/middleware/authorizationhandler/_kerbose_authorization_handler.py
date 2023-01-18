"""Houses Kerbose Authorization Handler"""

from typing import Optional, TypeVar, Union, Tuple, Mapping
from requests import PreparedRequest, Response
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
from pyrestsdk.middleware import BaseAuthorizationHandler
from pyrestsdk.credential import AbstractKerbroseCredential
from pyrestsdk.type.enum import FeatureUsageFlag

T = TypeVar("T", bound=AbstractKerbroseCredential)
A = TypeVar("A", bound="KerboseAuthorizationHandler")


class KerboseAuthorizationHandler(BaseAuthorizationHandler):
    """Kerbose Authorization Handler Type"""

    credential: T

    def __init__(self, credential: T, **kwargs) -> None:
        super().__init__(credential, **kwargs)

    def send(
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
        """Makes a network request if next is none, otherwise requests the next middleware to do so

        Args:
            request (PreparedRequest): The network request

        Returns:
            Response: Response from network request
        """

        context = request.context  # type: ignore

        # TODO break dependancy for requests_kerberos module
        request.prepare_auth(
            HTTPKerberosAuth(
                mutual_authentication=OPTIONAL, principal=self._get_principle()
            )
        )

        context.set_feature_usage = FeatureUsageFlag.AUTH_HANDLER_ENABLED
        response = super().send(request, stream, timeout, verify, cert, proxies)

        # Token might have expired just before transmission, retry the request one more time
        if response.status_code == 401 and self.retry_count < 2:
            self.retry_count += 1
            return self.send(request, stream, timeout, verify, cert, proxies)
        return response

    def _get_principle(self: A) -> str:
        """Gets the encoded string from the credential's get_principle() function"""

        return self.credential.get_principle()
