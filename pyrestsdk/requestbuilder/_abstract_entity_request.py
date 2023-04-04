"""Houses Entity Request Builder"""

from __future__ import annotations

from typing import TypeVar, Iterable, Optional

from abc import abstractmethod

from pyrestsdk.requestbuilder._abstract_request_builder import AbstractRequestBuilder
from pyrestsdk.request import BaseRequest
from pyrestsdk.type.model import Option

R = TypeVar("R", bound=BaseRequest)
O = TypeVar("O", bound=Option)


class AbstractEntityRequestBuilder(AbstractRequestBuilder):
    """Entity Request Builder Type"""

    @property
    @abstractmethod
    def request(self) -> R:
        """Builds request with no options"""

    @abstractmethod
    def request_with_options(self, options: Optional[Iterable[O]]) -> R:
        """Builds request"""
