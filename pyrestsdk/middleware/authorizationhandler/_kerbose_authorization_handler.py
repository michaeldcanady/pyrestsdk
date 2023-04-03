"""Houses Kerbose Authorization Handler"""

from pyrestsdk.middleware.authorizationhandler._authorization_handler import (
    AuthorizationHandler,
)


class KerboseAuthorizationHandler(AuthorizationHandler):
    """Kerbose Authorization Handler Type"""

    def _get_auth_header(self) -> str:
        from requests_kerberos import ( # pylint: disable=import-outside-toplevel
            HTTPKerberosAuth,
            OPTIONAL,
        )

        kerbose_auth = HTTPKerberosAuth(
            mutual_authentication=OPTIONAL, principal=self.credential.get_principle()
        )

        return f"Kerberos {kerbose_auth}"
