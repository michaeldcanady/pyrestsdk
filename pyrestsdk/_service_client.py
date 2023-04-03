"""
Service Client
==============

"""

from abc import abstractmethod, ABC

from requests import Session, Response

from pyrestsdk._abstract_service_client import AbstractServiceClient

class ServiceClient(AbstractServiceClient, ABC):
    """
    Service Client Type
    """

    _session: Session = None

    @property
    def session(self) -> Session:
        """Gets the current session

        Returns:
            Session: The current session
        """

        return self._session

    def get(self, url: str, **kwargs) -> Response:
        """Sends a GET request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.session.get(self._instance_url(url), **kwargs)

    def options(self, url, **kwargs) -> Response:
        """Sends a OPTIONS request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.session.options(self._instance_url(url), **kwargs)

    def head(self, url, **kwargs) -> Response:
        """Sends a HEAD request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.session.head(self._instance_url(url), **kwargs)

    def post(self, url, data=None, json=None, **kwargs) -> Response:
        """Sends a POST request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        return self.session.post(self._instance_url(url), data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs) -> Response:
        """Sends a PUT request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        return self.session.put(self._instance_url(url), data=data, **kwargs)

    def patch(self, url, data=None, **kwargs) -> Response:
        """Sends a PATCH request. Returns :class:`Response` object.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        return self.session.patch(self._instance_url(url), data=data, **kwargs)

    def delete(self, url: str, **kwargs) -> Response:
        """Sends a DELETE request.
        
        Args:
            url (str): URL for the new :class:`Request` object.
            \*\*kwargs: Optional arguments that ``request`` takes.
        
        Returns:
            requests.Response: HTTP Response from request
        """
        return self.session.delete(self._instance_url(url), **kwargs)

    def _instance_url(self, url: str) -> str:
        """Joins session base URL with relative segement provided
        
        Args:
            url (str): The relative url from the base URL `/*/*` or `*/*`
        
        Returns:
            str: The Instance URL
        """

        return self.session.base_url + url if (url[0] == '/') else f"/{url}"  # type: ignore

    @staticmethod
    @abstractmethod
    def _get_session(*args, **kwargs) -> Session:
        """Gets the Session

        Returns:
            Session: The Session
        """
