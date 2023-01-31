from typing import Union

from base64 import b64encode

from pyrestsdk.credential._abstract_basic_credential import AbstractBasicCredential

class BasicCredential(AbstractBasicCredential):
    """Basic Authentication Credential Type"""
    
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
        
    def to_native_string(self, string: Union[str, bytes], encoding="ascii") -> str:
        
        if isinstance(string, str):
            return string
        
        return string.decode(encoding)
    
    def get_basic(self, /) -> str:
        
        username = self.username.encode("latin1")
        password = self.password.encode("latin1")

        return self.to_native_string(b64encode(b":".join((username, password))).strip())