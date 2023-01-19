"""Supports Types"""

from pyrestsdk.request.supports_types._supports_base_invoke_request import (
    SupportsBaseInvokeRequest,
)
from pyrestsdk.request.supports_types._supports_invoke_collection_request import (
    SupportsInvokeCollectionRequest,
)
from pyrestsdk.request.supports_types._supports_invoke_request import (
    SupportsInvokeRequest,
)

from pyrestsdk.request.supports_types._supports_delete_method import (
    SupportsDeleteMethod,
)
from pyrestsdk.request.supports_types._supports_get_method import SupportsGetMethod
from pyrestsdk.request.supports_types._supports_post_method import SupportsPostMethod
from pyrestsdk.request.supports_types._supports_put_method import SupportsPutMethod

__all__ = [
    "SupportsInvokeRequest",
    "SupportsBaseInvokeRequest",
    "SupportsInvokeCollectionRequest",
    "SupportsDeleteMethod",
    "SupportsGetMethod",
    "SupportsPostMethod",
    "SupportsPutMethod",
]
