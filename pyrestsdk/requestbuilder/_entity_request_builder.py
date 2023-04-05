"""Houses Entity Request Builder"""

from __future__ import annotations

from typing import TypeVar

from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.requestbuilder._abstract_entity_request import (
    AbstractEntityRequestBuilder,
)

from pyrestsdk.request import BaseRequest
from pyrestsdk import ServiceClient

R = TypeVar("R", bound=BaseRequest)
B = TypeVar("B", bound="AbstractEntityRequestBuilder")
S = TypeVar("S", bound=ServiceClient)


class EntityRequestBuilder(AbstractEntityRequestBuilder, BaseRequestBuilder):
    """Entity Request Builder Type"""

    @property
    def request(self) -> R:

        return self.request_with_options(None)
