"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

import base64

class BasicAuthMixin: #pylint: disable=too-few-public-methods
    """
    Basic Authentication Mixin
    ==========================
    
    Mixin class for Basic authentication.
    
    Usage::
        from pyrestsdk.credential.mixins import BasicAuthMixin
        
        # Define new class using the mixin
        class ExampleCredential(BasicAuthMixin):
            
            def __init__(self, username: str, password: str):
                BasicAuthMixin().__init__(username, password)
        
        # Create instance of credential        
        credential = ExampleCredential("example","password")
        
        credential._get_encoded_basic_auth_header()
    """

    def __init__(self, username: str, password: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._username = username
        self._password = password

    def _get_encoded_basic_auth_header(self) -> str:
        _encode_string = f"{self._username}:{self._password}".encode("ascii")
        _base64_string = base64.b64encode(_encode_string)
        _decode_base64_string = _base64_string.decode("ascii")

        return f"Basic {_decode_base64_string}"
