"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from pyrestsdk.credential._abstract_kerbrose_credential import AbstractKerbroseCredential

class KerberosCredential(AbstractKerbroseCredential): #pylint: disable=too-few-public-methods
    """
    Kerberos Credential
    ===================
    
    
    """

    def __init__(self, username: str, password: str):

        self.username = username
        self.password = password

    def get_principle(self) -> str: #pylint: disable=arguments-differ

        return f"{self.username}:{self.password}"
