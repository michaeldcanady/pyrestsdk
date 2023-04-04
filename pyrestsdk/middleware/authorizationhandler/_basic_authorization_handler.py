"""Houses Basic Authorization Handler"""

from pyrestsdk.middleware.authorizationhandler._authorization_handler import AuthorizationHandler


class BasicAuthorizationHandler(AuthorizationHandler):
    """Basic Authoziation Handler Type"""

    def _get_auth_header(self) -> str:
        return f"Basic {self.credential.get_basic()}"
