from requests import PreparedRequest, Response
from typing import Union

# internal imports
from pyrestsdk.credential import AbstractTokenCredential, AbstractBasicCredential
from pyrestsdk._feature_usage_flag import FeatureUsageFlag
from ._base_middleware import BaseMiddleware


class AuthorizationHandler(BaseMiddleware):

    credential: Union[AbstractTokenCredential, AbstractBasicCredential]

    def __init__(self, credential: Union[AbstractTokenCredential, AbstractBasicCredential], **kwargs):
        super().__init__()
        self.credential = credential
        self.retry_count = 0

    def send(self, request: PreparedRequest, **kwargs) -> Response:
        """Makes a network request if next is none, otherwise requests the next middleware to do so

        Args:
            request (PreparedRequest): The network request

        Returns:
            Response: Response from network request
        """

        context = request.context  # type: ignore

        if issubclass(type(self.credential), AbstractTokenCredential):
            request.headers.update(
                {'Authorization': 'Bearer {}'.format(self._get_access_token(context))}
            )
        elif issubclass(type(self.credential), AbstractBasicCredential):
            request.headers.update(
                {'Authorization': 'Basic {}'.format(self._get_basic_auth())}
            )
        else:
            raise Exception(f"{type(self.credential)} is not valid must be subclass of: AbstractTokenCredential or AbstractBasicCredential")

        context.set_feature_usage = FeatureUsageFlag.AUTH_HANDLER_ENABLED
        response = super().send(request, **kwargs)

        # Token might have expired just before transmission, retry the request one more time
        if response.status_code == 401 and self.retry_count < 2:
            self.retry_count += 1
            return self.send(request, **kwargs)
        return response

    def _get_basic_auth(self, *args, **kwargs) -> str:
        """Gets the encoded string from the credential's get_basic() function

        Returns:
            str: The encoded string
        """

        if issubclass(type(self.credential), AbstractTokenCredential):
            raise Exception("AbstractTokenCredential does not support basic authentication")

        return self.credential.get_basic(*args, **kwargs) # type: ignore

    def _get_access_token(self, *args, **kwargs) -> str:
        """Gets the token from the credential's get_token() function

        Returns:
            str: The token
        """

        if issubclass(type(self.credential), AbstractBasicCredential):
            raise Exception("AbstractBasicCredential does not support token authentication")

        return self.credential.get_token(*args, **kwargs)[0]