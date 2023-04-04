"""Houses Token Authorization Handler"""

from pyrestsdk.middleware.authorizationhandler._authorization_handler import AuthorizationHandler


class TokenAuthorizationHandler(AuthorizationHandler):
    """Token Authorization Handler Type"""

    def _get_auth_header(self) -> str:
        return f"Bearer {self.credential.get_token()}"
