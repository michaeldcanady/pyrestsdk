"""Houses Base Request Builder"""

from __future__ import annotations
from typing import TypeVar
from pyrestsdk import AbstractServiceClient
from pyrestsdk.requestbuilder._abstract_request_builder import AbstractRequestBuilder


S = TypeVar("S", bound=AbstractServiceClient)
B = TypeVar("B", bound="BaseRequestBuilder")


class BaseRequestBuilder(AbstractRequestBuilder):
    """Base Request Builder Type"""
