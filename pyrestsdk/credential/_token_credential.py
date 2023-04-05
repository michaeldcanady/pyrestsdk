"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from abc import ABC

from pyrestsdk.credential._authenticator_client import AuthenticatorClient
from pyrestsdk.credential._abstract_token_credential import AbstractTokenCredential

class TokenAuthenticator(AbstractTokenCredential, ABC):
    """
    Token Authenticator
    =====================
    
    Base class for token-based API authentication.
    
    """

    def __init__(self, instance: str, hostname: str) -> None:

        self._base_url = self._get_base_url(instance, hostname)

        self._client = AuthenticatorClient()

    def _get_base_url(self, instance: str, hostname: str) -> str:
        """Gets the base authentication URL

        Args:
            instance (str): The instance of the Hostname
            hostname (str): The Hostname of the authentication URL

        Returns:
            str: The base authentication URL
        """

        return f"https://{instance}.{hostname}"

    def _append_segment_to_request_url(self, url_segment: str) -> str:
        """Appends a URL segment to the request URL.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self._base_url}{url_segment}"
