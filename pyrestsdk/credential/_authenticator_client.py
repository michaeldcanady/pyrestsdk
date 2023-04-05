"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from requests import Response, Session

class AuthenticatorClient:
    """
    Authenticator Client
    ====================

    Client class for handling API requests.
    """

    def __init__(self) -> None:
        self._session = Session()

    def post(self, url: str, params=None, data=None, headers=None) -> Response:
        return self._session.post(
            url=url,
            data=data,
            params=params,
            headers=headers
        )
