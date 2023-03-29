"""Houses MIME Types
"""

from enum import Enum, auto


class MIMECategoryEnum(str, Enum):
    """MIME Category Enum
    """

    def __new__(cls, value, *args, **kwargs):
        if not isinstance(value, (str, auto)):
            raise TypeError(
                f"Values of MIMECategoryEnum must be strings: {value!r} is a {type(value)}"
            )

        prefix = f"{cls.__name__.lower()}/"

        if isinstance(value, str) and not value.startswith(prefix):
            raise TypeError(
                f"Value of MIMECategoryEnum must begin with the designated prefix:{value!r} does not start with {prefix!r}"
            )

        return super().__new__(cls, value, *args, **kwargs)

    def __str__(self) -> str:

        return self.value


class MimeType:
    """MIME Type"""

    class Text(MIMECategoryEnum):
        """Text MIME Type"""

        PLAIN = "text/plain"
        HTML = "text/html"
        CSS = "text/css"
        JAVASCRIPT = "text/javascript"
        CSV = "text/csv"

    class Application(MIMECategoryEnum):
        """Application MIME Type"""

        OCTET_STREAM = "application/octet-stream"
        PKCS12 = "application/x-pkcs12"
        X_WWW_FORM_URLENCODED = "application/x-www-form-urlencoded"
        JSON = "application/json"
        PDF = "application/pdf"
        XML = "application/xml"
        ZIP = "application/zip"
        GZIP = "application/gzip"

    class Image(MIMECategoryEnum):
        """Image MIME Type"""

        JPEG = "image/jpeg"
        PNG = "image/png"
        GIF = "image/gif"
        SVG_XML = "image/svg+xml"
        WEBP = "image/webp"

    class Audio(MIMECategoryEnum):
        """Audio MIME Type"""

        MIDI = "audio/midi"
        MPEG = "audio/mpeg"
        WEBM = "audio/webm"
        OGG = "audio/ogg"
        WAV = "audio/wav"

    class Video(MIMECategoryEnum):
        """Video MIME Type"""

        MPEG = "video/mpeg"
        MP4 = "video/mp4"
        OGG = "video/ogg"
        WEBM = "video/webm"
        QUICKTIME = "video/quicktime"
