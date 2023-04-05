"""
Authorzation Handler Tests
==========================
"""
from unittest.mock import patch

from requests import PreparedRequest, Response

from pyrestsdk.credential import AbstractTokenCredential
from pyrestsdk.middleware.authorizationhandler import TokenAuthorizationHandler
from pyrestsdk.type.model.token import AccessToken

class MockTokenCredential(AbstractTokenCredential): #pylint: disable=too-few-public-methods
    """
    Mock Token Credential for testing
    """

    def get_token(self, *args, **kwargs) -> AccessToken: #pylint: disable=[arguments-differ,unused-argument]
        return AccessToken("test_token")

    def parse_token(self, response):
        pass

def test_token_authorization_handler():
    """
    Tests base implementation of authorization handler
    """

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
