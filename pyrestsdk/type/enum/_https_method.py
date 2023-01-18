"""Houses Https Method Enum"""

from enum import IntEnum, auto


class HttpsMethod(IntEnum):
    """HTTPS Method enum"""

    GET = auto()
    POST = auto()
    DELETE = auto()
    PATCH = auto()
    PUT = auto()


HttpsMethod.GET.__doc__ = """"""
HttpsMethod.POST.__doc__ = """"""
HttpsMethod.DELETE.__doc__ = """"""
HttpsMethod.PATCH.__doc__ = """"""
HttpsMethod.PUT.__doc__ = """"""
