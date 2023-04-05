"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk.credential._token_credential import TokenAuthenticator
from pyrestsdk.credential.mixins import BasicAuthMixin


class BasicTokenAuthenticator(TokenAuthenticator, BasicAuthMixin):
    """
    Basic Token Authenticator
    =========================

    Base class for Basic token-based API authentication.
    """

    def __init__( #pylint: disable=too-many-arguments
        self,
        instance: str,
        hostname: str,
        username: str,
        password: str,
        segment: str,
    ) -> None:
        TokenAuthenticator.__init__(self, instance, hostname)
        BasicAuthMixin.__init__(self, username, password)

        self._authentication_url = self._append_segment_to_request_url(
            segment
        )

    def get_token(self) -> str: # pylint: disable=arguments-differ
        """Gets Authentication Token

        Returns:
            str: Authentication Token
        """

        headers = {"Authorization": self._get_encoded_basic_auth_header()}

        return self.parse_token(
            self._client.post(self._authentication_url, headers=headers)
        )
