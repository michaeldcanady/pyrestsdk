"""Houses Base Request Builder"""

from __future__ import annotations
from typing import TypeVar
from pyrestsdk import AbstractServiceClient
from pyrestsdk.request._abstract_request import AbstractRequest

S = TypeVar("S", bound=AbstractServiceClient)
B = TypeVar("B", bound="BaseRequestBuilder")


class BaseRequestBuilder(AbstractRequest):
    """Base Request Builder Type"""
