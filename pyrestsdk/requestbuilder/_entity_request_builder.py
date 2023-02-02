"""Houses Entity Request Builder"""

from __future__ import annotations

from typing import TypeVar

from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.requestbuilder._abstract_entity_request import (
    AbstractEntityRequestBuilder,
)

from pyrestsdk.request import BaseRequest
from pyrestsdk import AbstractServiceClient

R = TypeVar("R", bound=BaseRequest)
B = TypeVar("B", bound="AbstractEntityRequestBuilder")
S = TypeVar("S", bound=AbstractServiceClient)


class EntityRequestBuilder(AbstractEntityRequestBuilder[R], BaseRequestBuilder[R]):
    """Entity Request Builder Type"""

    def __init__(self: B, request_url: str, client: S) -> None:
        super().__init__(request_url, client)

    @property
    def request(self) -> R:

        return self.request_with_options(None)
