"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from dataclasses import dataclass

@dataclass
class BaseToken:
    """
    Base Token
    ==========
    
    """

    _token: str

    @property
    def token(self) -> str:
        """Gets the token
        """

        return self._token


BaseToken.token.__doc__ = """The token string."""
