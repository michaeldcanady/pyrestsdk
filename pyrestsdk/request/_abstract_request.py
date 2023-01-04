from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Dict,
    TypeVar,
    Generic,
    Type,
    final,
    get_args
)

# Internal Imports
from pyrestsdk import AbstractServiceClient

B = TypeVar("B", bound="AbstractRequest")
S = TypeVar("S", bound="AbstractServiceClient")
T = TypeVar("T")

class AbstractRequest(Generic[T]):

    def __init__(self: B, request_url: str, client: S) -> None:
        
        super().__init__()

        self._request_url: str = request_url
        self._client: S = client

    @property
    def Client(self: B) -> S:
        return self._client
    
    @property
    @final
    def GenericType(self) -> Type[T]:
        """Gets the the type argument provided
        """
        
        _type: Type[T] = get_args(self.__orig_bases__[0])[0] # type: ignore  
              
        return _type

    @property
    def RequestUrl(self: B) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """

        return self._request_url

    @RequestUrl.setter
    def RequestUrl(self: B, value: str) -> None:
        self._request_url = value

    def AppendSegmentToRequestUrl(self, url_segment:str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """
        
        if not url_segment.startswith("/"):
            # Checks if url segment starts with /
            # Appends it if it does not
            url_segment = "/{0}".format(url_segment)
        
        return "{0}{1}".format(self.RequestUrl, url_segment)