"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk.type.model.token._base_token import BaseToken


class AccessToken(BaseToken):
    """
    Access Token
    ============
    
    """

    _expires_on: int

    @property
    def expires_on(self) -> int:
        """The token's expiration time in Unix time.
        """
        return self._expires_on
