"""Houses Feature Usage Flag Enum"""

from enum import IntEnum


class FeatureUsageFlag(IntEnum):
    """Enumerated list of values used to flag usage of specific middleware"""

    NONE = 0
    REDIRECT_HANDLER_ENABLED = 1
    RETRY_HANDLER_ENABLED = 2
    AUTH_HANDLER_ENABLED = 4
    DEFAULT_HTTP_PROVIDER_ENABLED = 8
    LOGGING_HANDLER_ENABLED = 16


FeatureUsageFlag.NONE.__doc__ = "No Feature Flags Set"
FeatureUsageFlag.REDIRECT_HANDLER_ENABLED.__doc__ = "Redirect Handler Enabled"
FeatureUsageFlag.AUTH_HANDLER_ENABLED.__doc__ = "Authorization Handler Enabled"
FeatureUsageFlag.DEFAULT_HTTP_PROVIDER_ENABLED.__doc__ = "Default HTTP Provider Enabled"
FeatureUsageFlag.LOGGING_HANDLER_ENABLED.__doc__ = "Logging Handler Enabled"
