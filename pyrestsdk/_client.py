"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from typing import Optional

from abc import ABC

from urllib3.util import parse_url

from requests import Session, Response

class Client(ABC):
    """
    Client
    ======
    
    The shared parent class that provides common functionality
    for making HTTP requests and handling URLs.
    
    Usage::
        from pyrestsdk._client import Client
        from requests import Session

        class ExampleClient(Client):
            def __init__(self, base_url: str):
                session = Session()
                session.base_url = base_url
                super().__init__(session)

        # Instantiate the ExampleClient with the JSONPlaceholder base URL
        example_client = ExampleClient("https://jsonplaceholder.typicode.com")

        # Send a GET request to retrieve a single user by ID (example: user with ID 1)
        response = example_client.get("/users/1")
    """

    def __init__(self, session: Optional[Session] = Session()) -> None:

        self._session = session

    @property
    def session(self) -> Session:
        """Gets the current session

        Returns:
            Session: The current session
        """

        return self._session

    def get(self, url: str, **kwargs) -> Response:
        """Sends a GET request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

        return self.session.get(self.get_resolved_url(url), **kwargs)

    def options(self, url: str, **kwargs) -> Response:
        """Sends a OPTIONS request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

        return self.session.options(self.get_resolved_url(url), **kwargs)

    def head(self, url: str, **kwargs) -> Response:
        """Sends a HEAD request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

        return self.session.head(self.get_resolved_url(url), **kwargs)

    def post(self, url: str, data=None, json=None, **kwargs) -> Response:
        """Sends a POST request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

        return self.session.post(
            self.get_resolved_url(url), data=data, json=json, **kwargs
        )

    def put(self, url: str, data=None, **kwargs) -> Response:
        """Sends a PUT request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

        return self.session.put(self.get_resolved_url(url), data=data, **kwargs)

    def patch(self, url: str, data=None, **kwargs) -> Response:
        """Sends a PATCH request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

        return self.session.patch(self.get_resolved_url(url), data=data, **kwargs)

    def delete(self, url: str, **kwargs) -> Response:
        """Sends a DELETE request.

        Args:
            url (str): The URL for the request.
            **kwargs: Optional keyword arguments for the request.

        Returns:
            Response: The server's response.
        """

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

        if getattr(self.session, "base_url", None) is None and self._is_complete_url(url):
            return url

        input_url = parse_url(url)
        proper_url = parse_url(self.session.base_url)

        if self._is_complete_url(url):
            if input_url.host == proper_url.host:
                return url
            else:
                raise ValueError(
                    f"URL {url} doesn't start with the expected base URL {self.session.base_url}"
                )

        # If the URL is a segment, use the append_segment_to_request_url method
        return self._append_segment_to_request_url(url)

    def _is_complete_url(self, url: str) -> bool:
        """Checks if the given URL is a complete URL.

        Args:
            url (str): The URL to be checked.

        Returns:
            bool: True if the URL is a complete URL, False otherwise.
        """
        parsed_url = parse_url(url)
        return parsed_url.host is not None

    def _append_segment_to_request_url(self, url_segment: str) -> str:
        """Gets a URL that is the request URL with the segment appended.

        Args:
            url_segment (str): The segment to append to the request URL.

        Returns:
            str: A URL that is the request URL with the segment appended.
        """

        if not url_segment.startswith("/"):
            url_segment = f"/{url_segment}"

        return f"{self.session.base_url}{url_segment}"
