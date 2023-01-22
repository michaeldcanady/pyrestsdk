"""Houses Base Token"""

from dataclasses import dataclass

@dataclass
class BaseToken:
    """Base Token Type"""

    _token: str
    
    @property
    def token(self) -> str:
        return self._token


BaseToken.token.__doc__ = """The token string."""
