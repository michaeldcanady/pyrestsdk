"""House Abstract Service Client"""

from typing import TypeVar, Type
from abc import ABC, abstractmethod
from requests import Response, Session


S = TypeVar("S", bound="AbstractServiceClient")


class AbstractServiceClient(ABC):
    """Abstract Service Client Type"""

    def __new__(cls: Type[S], *args, **kwargs) -> S:
        if getattr(AbstractServiceClient, "__instance", None) is None:
            AbstractServiceClient.__instance = object.__new__(cls)
        return AbstractServiceClient.__instance

    @abstractmethod
    def get(self, url: str, **kwargs) -> Response:
        r"""Sends a GET request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def options(self, url: str, **kwargs) -> Response:
        r"""Sends a OPTIONS request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def head(self, url: str, **kwargs) -> Response:
        r"""Sends a HEAD request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def post(self, url: str, data=None, json=None, **kwargs) -> Response:
        r"""Sends a POST request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def put(self, url: str, data=None, **kwargs) -> Response:
        r"""Sends a PUT request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def patch(self, url: str, data=None, **kwargs) -> Response:
        r"""Sends a PATCH request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def delete(self, url: str, **kwargs) -> Response:
        r"""Sends a DELETE request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

    @abstractmethod
    def _get_session(self, /, **kwargs) -> Session:
        """Method to always retrun a single instance of an HTTP Client"""

    @abstractmethod
    def _instance_url(self, url: str) -> str:
        """Appends BASE_URL to user provided path
        :param url: user provided path
        :return: graph_url
        """
