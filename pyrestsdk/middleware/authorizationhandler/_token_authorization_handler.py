"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk.middleware.authorizationhandler._authorization_handler import AuthorizationHandler


class TokenAuthorizationHandler(AuthorizationHandler):
    """
    Token Authorization Handler
    ===========================
    
    """

    def _get_auth_header(self) -> str:
        return f"Bearer {self.credential.get_token()}"
