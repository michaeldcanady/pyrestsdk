"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk._client import Client

class AuthenticatorClient(Client):
    """
    Authenticator Client
    ====================

    Client class for handling API requests.
    """

    def __init__(self) -> None:
        super().__init__(None)
