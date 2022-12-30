from pyrestsdk.type.model.token._base_token import BaseToken

class AccessToken(BaseToken):
    expires_on: int

#AccessToken.expires_on.__doc__ = """The token's expiration time in Unix time."""