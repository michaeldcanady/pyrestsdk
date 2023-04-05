"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from abc import abstractmethod

from typing import TypeVar

from requests import Response

from pyrestsdk.credential._abstract_credential import AbstractCredential
from pyrestsdk.type.model.token import AccessToken

A = TypeVar("A", bound=AccessToken)


class AbstractTokenCredential(AbstractCredential): #pylint: disable=too-few-public-methods
    """Abstract Token Credential Type"""

    @abstractmethod
    def get_token(self, /) -> A:
        """Gets the access token"""

    @abstractmethod
    def parse_token(self, response: Response) -> str:
        """Parses response into Token string

        Args:
            response (Response): Response containing the token

        Returns:
            str: the Token string
        """
