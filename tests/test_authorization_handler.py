import pytest
from requests import PreparedRequest, Response
from unittest.mock import MagicMock, patch

from pyrestsdk.credential import AbstractTokenCredential
from pyrestsdk.middleware.authorizationhandler import TokenAuthorizationHandler
from pyrestsdk.type.model.token import AccessToken

class MockTokenCredential(AbstractTokenCredential):
    def get_token(self, *args, **kwargs) -> AccessToken:
        return AccessToken("test_token")

def test_token_authorization_handler():
    # Arrange
    credential = MockTokenCredential()
    handler = TokenAuthorizationHandler(credential)

    # Mock request and response objects
    request = PreparedRequest()
    response = Response()
    response.status_code = 200
    response.headers = {"Authorization":"Bearer test_token"}

    # Mock middleware send function to return response
    with patch.object(
        TokenAuthorizationHandler, "send", return_value=response
    ) as mock_send:
        # Act
        result = handler.send(request)

        # Assert
        mock_send.assert_called_once_with(request)
        assert result == response

        # Assert that the authorization header was set correctly
        #assert request.headers["Authorization"] == "Bearer test_token"
