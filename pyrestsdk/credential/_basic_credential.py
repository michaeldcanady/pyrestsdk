from typing import Union

from base64 import b64encode

from pyrestsdk.credential._abstract_basic_credential import AbstractBasicCredential

class BasicCredential(AbstractBasicCredential):
    """Basic Authentication Credential Type"""

    def to_native_string(self, string: Union[str, bytes], encoding="ascii") -> str:
        """Converts native to string

        Args:
            string (Union[str, bytes]): The string to convert
            encoding (str, optional): The encoding type. Defaults to "ascii".

        Returns:
            str: The converted string
        """

        if isinstance(string, str):
            return string

        return string.decode(encoding)

    def get_basic(self, /) -> str:
        """Gets the basic auth header value

        Returns:
            str: The basic auth header value
        """

        username = self.username.encode("latin1")
        password = self.password.encode("latin1")

        return self.to_native_string(b64encode(b":".join((username, password))).strip())
