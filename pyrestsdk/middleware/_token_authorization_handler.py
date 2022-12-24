from typing import TypeVar
from requests import PreparedRequest, Response

# internal imports
from pyrestsdk.middleware._base_authorization_handler import BaseAuthorizationHandler
from pyrestsdk.credential import AbstractTokenCredential
from pyrestsdk.type.enum import FeatureUsageFlag

T = TypeVar("T", bound=AbstractTokenCredential)
A = TypeVar("A", bound="TokenAuthorizationHandler")


class TokenAuthorizationHandler(BaseAuthorizationHandler):

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
                {"Authorization": "Bearer {}".format(self._get_access_token(context))}
            )

        context.set_feature_usage = FeatureUsageFlag.AUTH_HANDLER_ENABLED
        response = super().send(request, **kwargs)

        # Token might have expired just before transmission, retry the request one more time
        if response.status_code == 401 and self.retry_count < 2:
            self.retry_count += 1
            return self.send(request, **kwargs)
        return response

    def _get_access_token(self: A, *args, **kwargs) -> str:
        """Gets the token from the credential's get_token() function

        Returns:
            str: The token
        """

        return self.credential.get_token(*args, **kwargs).token
