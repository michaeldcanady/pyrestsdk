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

        return self.session.get(self._instance_url(url), **kwargs)

    def options(self, url, **kwargs) -> Response:

        return self.session.options(self._instance_url(url), **kwargs)

    def head(self, url, **kwargs) -> Response:

        return self.session.head(self._instance_url(url), **kwargs)

    def post(self, url, data=None, json=None, **kwargs) -> Response:

        return self.session.post(self._instance_url(url), data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs) -> Response:

        return self.session.put(self._instance_url(url), data=data, **kwargs)

    def patch(self, url, data=None, **kwargs) -> Response:

        return self.session.patch(self._instance_url(url), data=data, **kwargs)

    def delete(self, url: str, **kwargs) -> Response:

        return self.session.delete(self._instance_url(url), **kwargs)

    def _instance_url(self, url: str) -> str:

        return self.session.base_url + url if (url[0] == '/') else f"/{url}"  # type: ignore

    @staticmethod
    @abstractmethod
    def _get_session(*args, **kwargs) -> Session:
        """Gets the Session

        Returns:
            Session: The Session
        """

    def append_segment_to_request_url(self, url_segment: str) -> None:
        """Gets a URL that is the request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self.session.base_url}{url_segment}"
