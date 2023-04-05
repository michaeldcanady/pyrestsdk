"""
------------------------------------
Copyright (c) Michael Canady.
Licensed under the MIT License.
------------------------------------
"""

from abc import abstractmethod, ABC

from requests import Session

from pyrestsdk._client import Client


class ServiceClient(Client, ABC):
    """
    Service Client
    ==============
    
    A base class for creating service-specific clients,
    providing common functionality and enforcing a standard interface.

    The ServiceClient class is intended to be subclassed by specific
    service client implementations. By extending this class,
    a service client will inherit common functionality for
    handling HTTP requests and managing sessions while providing
    a consistent interface to interact with various APIs.

    Usage::

        class ExampleServiceClient(ServiceClient):

            def __init__(self):
                super().__init__()

            @staticmethod
            def _get_session(*args, **kwargs) -> Session:
                # Implementation for retrieving the session

            @staticmethod
            def _initialize_session_and_base_url(*args, **kwargs) -> Session:
                # Implementation for initializing the session and base URL

        # Usage of the ExampleServiceClient
        example_client = ExampleServiceClient()
        response = example_client.get("/endpoint")

    """

    @staticmethod
    @abstractmethod
    def _get_session(*args, **kwargs) -> Session:
        """Gets the Session

        Returns:
            Session: The Session
        """

    @staticmethod
    @abstractmethod
    def _initialize_session_and_base_url(*args, **kwargs) -> Session:
        """Initialize the session and base URL for the ServiceClient.

        Returns:
            Session: The session
        """

        raise NotImplementedError(
            "Derived classes must implement the _initialize_session_and_base_url method."
        )
