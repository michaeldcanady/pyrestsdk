"""
Service Client
==============

"""
from typing import Optional

from abc import abstractmethod, ABC

from urllib3.util import parse_url

from requests import Session, Response

from pyrestsdk._abstract_service_client import AbstractServiceClient


class ServiceClient(AbstractServiceClient, ABC):
    """
    Service Client Type
    """

    def __init__(self, session: Optional[Session] = None) -> None:

        super().__init__()

        self._session = session

    @property
    def session(self) -> Session:
        """Gets the current session

        Returns:
            Session: The current session
        """

        return self._session

    def get(self, url: str, **kwargs) -> Response:
        return self.session.get(self.get_resolved_url(url), **kwargs)

    def options(self, url, **kwargs) -> Response:
        return self.session.options(self.get_resolved_url(url), **kwargs)

    def head(self, url, **kwargs) -> Response:
        return self.session.head(self.get_resolved_url(url), **kwargs)

    def post(self, url, data=None, json=None, **kwargs) -> Response:
        return self.session.post(
            self.get_resolved_url(url), data=data, json=json, **kwargs
        )

    def put(self, url, data=None, **kwargs) -> Response:
        return self.session.put(self.get_resolved_url(url), data=data, **kwargs)

    def patch(self, url, data=None, **kwargs) -> Response:
        return self.session.patch(self.get_resolved_url(url), data=data, **kwargs)

    def delete(self, url: str, **kwargs) -> Response:
        return self.session.delete(self.get_resolved_url(url), **kwargs)

    def get_resolved_url(self, url: str) -> str:
        """
        Determine if the given URL is a segment or a complete URL.
        If it's a segment, append it to self.session.base_url.
        If it's a complete URL, ensure it begins with self.session.base_url.

        Args:
            url (str): The URL to be checked.

        Returns:
            str: The full URL if the input is a segment, or the original URL if it's a complete URL.

        Raises:
            ValueError: If the URL is a full URL but doesn't start with self.session.base_url.
        """

        input_url = parse_url(url)
        proper_url = parse_url(self.session.base_url)

        if self.is_complete_url(url):
            if input_url.host == proper_url.host:
                return url
            else:
                raise ValueError(
                    f"URL {url} doesn't start with the expected base URL {self.session.base_url}"
                )

        # If the URL is a segment, use the append_segment_to_request_url method
        return self.append_segment_to_request_url(url)

    def is_complete_url(self, url: str) -> bool:
        """Checks if the given URL is a complete URL.

        Args:
            url (str): The URL to be checked.

        Returns:
            bool: True if the URL is a complete URL, False otherwise.
        """
        parsed_url = parse_url(url)
        return parsed_url.host is not None

    @staticmethod
    @abstractmethod
    def _get_session(*args, **kwargs) -> Session:
        """Gets the Session

        Returns:
            Session: The Session
        """

    def append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self.session.base_url}{url_segment}"
