from typing import Optional, TypeVar
from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter

B = TypeVar('B', bound='BaseMiddleware')

class BaseMiddleware(HTTPAdapter):
    """Base class for middleware

    Handles moving a Request to the next middleware in the pipeline.
    If the current middleware is the last one in the pipeline, it
    makes a network request
    """

    next: Optional[B] = None

    def __init__(self):
        super().__init__()

    def send(self: B, request: PreparedRequest, **kwargs) -> Response:
        """Makes a network request if next is none, otherwise requests the next middleware to do so

        Args:
            request (PreparedRequest): The network request

        Returns:
            Response: Response from network request
        """

        if self.next is None:
            return super().send(request, **kwargs)
        return self.next.send(request, **kwargs)
