"""Houses Basic Authorization Handler"""

from typing import TypeVar
from requests import PreparedRequest, Response
from pyrestsdk.middleware._base_authorization_handler import BaseAuthorizationHandler
from pyrestsdk.credential import AbstractBasicCredential
from pyrestsdk.type.enum import FeatureUsageFlag

T = TypeVar("T", bound=AbstractBasicCredential)
A = TypeVar("A", bound="BasicAuthorizationHandler")


class BasicAuthorizationHandler(BaseAuthorizationHandler):
    """Basic Authoziation Handler Type"""

    credential: T

    def __init__(self, credential: T, **kwargs) -> None:
        super().__init__(credential, **kwargs)

    def send(self: A, request: PreparedRequest, **kwargs) -> Response:
        """Makes a network request if next is none, otherwise requests the next middleware to do so

        Args:
            request (PreparedRequest): The network request

        Returns:
            Response: Response from network request
        """

        context = request.context  # type: ignore

        request.headers.update(
                {'Authorization': 'Basic {}'.format(self._get_basic_auth())}
            )

        context.set_feature_usage = FeatureUsageFlag.AUTH_HANDLER_ENABLED
        response = super().send(request, **kwargs)

        # Token might have expired just before transmission, retry the request one more time
        if response.status_code == 401 and self.retry_count < 2:
            self.retry_count += 1
            return self.send(request, **kwargs)
        return response

    def _get_basic_auth(self: A, /) -> str:
        """Gets the encoded string from the credential's get_basic() function

        Returns:
            str: The encoded string
        """

        return self.credential.get_basic()