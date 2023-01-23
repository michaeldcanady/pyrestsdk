from typing import TypeVar
from typing import (
    final,
    TypeVar,
    List,
    Union,
    Type,
    Optional,
    Iterable,
    get_args,
    Dict,
    Any,
)
from abc import abstractmethod
import logging
from urllib.parse import urlparse
from requests import Response
from pyrestsdk import AbstractServiceClient
from pyrestsdk.request._abstract_request import AbstractRequest
from pyrestsdk.type.enum import HttpsMethod
from pyrestsdk.type.model import (
    BaseEntity,
    QueryOption,
    HeaderOption,
    HeaderOptionCollection,
    QueryOptionCollection,
)
from pyrestsdk.request._abstract_request import AbstractRequest

T = TypeVar("T")
B = TypeVar("B", bound="Request")
O = TypeVar("O", QueryOption, HeaderOption)
S = TypeVar("S", bound=AbstractServiceClient)

Logger = logging.getLogger(__name__)


class Request(AbstractRequest[T]):

    _method: HttpsMethod
    _request_url: str
    _query_options: QueryOptionCollection
    _header_options: HeaderOptionCollection

    def __init__(
        self: B, request_url: str, client: S, options: Optional[Iterable[O]]
    ) -> None:

        super().__init__(request_url, client)

        self._method: HttpsMethod = HttpsMethod.GET
        self._request_url: str = self._initialize_url(request_url)
        self._query_options: QueryOptionCollection = QueryOptionCollection()
        self._header_options: HeaderOptionCollection = HeaderOptionCollection()
        self._parse_options(options)
    
    @property
    def header_options(self) -> HeaderOptionCollection:
        """Gets the headers"""
        return self._header_options

    @property
    def request_method(self) -> HttpsMethod:
        """Gets/Sets the https method"""
        return self._method

    @request_method.setter
    def request_method(self, value: HttpsMethod) -> None:
        self._method = value
        Logger.info("%s.Method: request method set to %s", type(self).__name__, value)

    @property
    def request_url(self: B) -> str:
        """Gets/Sets the request URL

        Returns:
            str: The request URL
        """

        return self._request_url

    @request_url.setter
    def request_url(self: B, value: str) -> None:
        self._request_url = value
        Logger.info("%s.request_url: request URL set to %s", type(self).__name__, value)

    @property
    @final
    def generic_type(self: B) -> Type[T]:

        # used if type arg is provided in constructor
        orig_value = getattr(self, "__orig_class__", None)

        if orig_value is None:
            # used if typ arg is provided when subclassing
            orig_bases = getattr(self, "__orig_bases__")
            orig_value = orig_bases[0]

        _type: Type[T] = get_args(orig_value)[0]

        return _type

    @property
    def Client(self: B) -> S:
        """Gets the Client"""

        return self._client

    def _initialize_url(self, request_url: str) -> str:
        """Parses the query parameters from URL"""

        Logger.info(f"%s._initialize_url: function called", type(self).__name__)

        if not request_url:
            pass

        url = urlparse(request_url)

        if url.query:
            query_string = url.query
            query_options = query_string.split("&")
            for option in query_options:
                query_parameter, value = option.split("=")
                _query_parameter = QueryOption(query_parameter, value)
                self.query_options.append(_query_parameter)

        return url._replace(query="").geturl()

    def Send(self, __object: Optional[Union[T, Dict[str, Any]]]) -> Optional[Union[List[T], T]]:
        """Submits the request and returns the expected return"""

        Logger.info("%s.Send: method called", type(self).__name__)

        return self.send_request(__object)

    def send_request(self, value: Optional[Union[T, Dict[str, Any]]]) -> Optional[Union[List[T], T]]:
        """Makes the desired request and returns the desired return type"""

        Logger.info("%s.SendRequest: method called", type(self).__name__)

        _response = self._send_request(value)

        if _response is None:
            return None

        return self.parse_response(_response)

    @abstractmethod
    def parse_response(
        self, _response: Optional[Response]
    ) -> Optional[Union[List[T], T]]:
        """Parses the response into the expected return"""

    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request builder's request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request builder's request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self.request_url}{url_segment}"
