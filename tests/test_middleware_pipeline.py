from pyrestsdk.middleware import MiddlewarePipeline, BaseMiddleware
from requests import PreparedRequest, Response


class TestMiddleware(BaseMiddleware):

    def prepare_request(self, request: PreparedRequest) -> PreparedRequest:
        request.headers["X-Test-Header"] = "Test"
        return request

    def handle_response(self, response: Response) -> Response:
        response.headers["X-Test-Response-Header"] = "Test"
        return response


def test_middleware_pipeline_add_middleware():
    pipeline = MiddlewarePipeline()
    middleware = TestMiddleware()
    pipeline.add_middleware(middleware)

    assert len(pipeline.middleware) == 1
    assert isinstance(pipeline.middleware[0], TestMiddleware)


def test_middleware_pipeline_execute():
    pipeline = MiddlewarePipeline()
    middleware = TestMiddleware()
    pipeline.add_middleware(middleware)

    request = PreparedRequest()
    response = Response()
    response.headers = {}

    pipeline.execute(request, lambda req: response)

    assert request.headers["X-Test-Header"] == "Test"
    assert response.headers["X-Test-Response-Header"] == "Test"
