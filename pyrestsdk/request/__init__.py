"""Requests"""
from sys import version_info
from pyrestsdk.request._request import Request

if version_info < (3,10):
    from pyrestsdk.request._base_request39 import BaseRequest
else:
    from pyrestsdk.request._base_request310 import BaseRequest

__all__ = ["BaseRequest", "Request"]
