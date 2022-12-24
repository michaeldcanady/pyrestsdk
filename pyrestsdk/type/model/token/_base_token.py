from typing import NamedTuple

class BaseToken(NamedTuple):

    token: str

BaseToken.token.__doc__ = """The token string."""