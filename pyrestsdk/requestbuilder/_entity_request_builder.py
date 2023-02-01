"""Houses Entity Request Builder"""

from __future__ import annotations

from typing import TypeVar, get_args, final, Type

from pyrestsdk.requestbuilder._base_request_builder import BaseRequestBuilder
from pyrestsdk.requestbuilder._abstract_entity_request import (
    AbstractEntityRequestBuilder,
)

from pyrestsdk.request import BaseRequest

R = TypeVar("R", bound=BaseRequest)
B = TypeVar("B", bound="AbstractEntityRequestBuilder")


class EntityRequestBuilder(AbstractEntityRequestBuilder[R], BaseRequestBuilder):
    """Entity Request Builder Type"""

    def __init__(self: B, request_url: str, client: S) -> None:
        super().__init__(request_url, client)


    @property
    @final
    def generic_type(self) -> Type[R]:

        # used if type arg is provided in constructor
        orig_value = getattr(self, "__orig_class__", None)

        if orig_value is None:
            # used if typ arg is provided when subclassing
            orig_bases = getattr(self, "__orig_bases__")
            orig_value = orig_bases[0]

        _type: Type[R] = get_args(orig_value)[0]

        return _type

    @property
    def request(self) -> R:

        return self.request_with_options(None)
