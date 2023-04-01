"""
Test Middleware pipeline
========================

Tests for the MiddlewarePipeline class
"""

import pytest

from requests import PreparedRequest, Response
from pyrestsdk.middleware._base_middleware import BaseMiddleware
from pyrestsdk.middleware._middleware_pipeline import MiddlewarePipeline

class MockMiddleware(BaseMiddleware):
    """Mock Middleware for testing
    """

    def __init__(self) -> None:
        self.next = None

    def send(
        self,
        request: PreparedRequest,
        stream: bool = False,
        timeout=None,
        verify: bool = True,
        cert=None,
        proxies=None,
    ) -> Response:
        if self.next is not None:
            self.next.send(
                request, stream, timeout, verify, cert, proxies
            )
        return Response()

def test_middleware_pipeline():
    """Tests that MiddlewarePipeline executes a chain of middlewares correctly
    """

    # Arrange
    middleware1 = MockMiddleware()
    middleware2 = MockMiddleware()
    middleware3 = MockMiddleware()

    middleware_pipeline = MiddlewarePipeline()
    middleware_pipeline.add_middleware(middleware1)
    middleware_pipeline.add_middleware(middleware2)
    middleware_pipeline.add_middleware(middleware3)

    # Act
    request = PreparedRequest()
    request.url = "http://example.com"
    request.method = "GET"
    headers = {"middleware_control": '{"key": "value"}'}
    request.headers = headers
    middleware_pipeline.send(request)

    # Assert
    assert middleware1.next == middleware2
    assert middleware2.next == middleware3
    assert middleware3.next is None


def test_middleware_pipeline_no_middleware():
    """Tests that MiddlewarePipeline raises a TypeError when there is no middleware in the pipeline
    """

    # Arrange
    middleware_pipeline = MiddlewarePipeline()

    # Act/Assert
    with pytest.raises(TypeError):
        middleware_pipeline.send(None)


def test_middleware_pipeline_one_middleware():
    """Tests that MiddlewarePipeline executes a single middleware correctly
    """

    # Arrange
    middleware1 = MockMiddleware()

    middleware_pipeline = MiddlewarePipeline()
    middleware_pipeline.add_middleware(middleware1)

    # Act
    request = PreparedRequest()
    request.url = "http://example.com"
    request.method = "GET"
    response = middleware_pipeline.send(request)

    # Assert
    assert middleware1.next is None
    assert response is not None

def test_middleware_pipeline_add_middleware_no_arguments():
    """Tests that MiddlewarePipeline raises a TypeError
    when add_middleware is called with no arguments
    """

    # Arrange
    middleware_pipeline = MiddlewarePipeline()

    # Act/Assert
    with pytest.raises(TypeError):
        middleware_pipeline.add_middleware()


def test_middleware_pipeline_add_middleware_non_base_middleware_argument():
    """Tests that MiddlewarePipeline raises a TypeError
    when add_middleware is called with a non-BaseMiddleware argument
    """

    # Arrange
    middleware_pipeline = MiddlewarePipeline()

    # Act/Assert
    with pytest.raises(TypeError):
        middleware_pipeline.add_middleware("Invalid Middleware")
