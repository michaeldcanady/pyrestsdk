from enum import IntEnum, auto

class HttpsMethod(IntEnum):
    GET = auto()
    POST = auto()
    DELETE = auto()
    PATCH = auto()
    PUT = auto()