from strenum import LowercaseStrEnum
from enum import auto
from typing import final, List, overload


class MediaTypeType(LowercaseStrEnum):

    Application = auto()
    Audio = auto()
    Image = auto()
    Text = auto()
    Video = auto()
    Font = auto()


class MediaTypeObject(object):
    
    @overload
    def __init__(self) -> None:...
    
    @overload
    def __init__(self, _type: MediaTypeType, _subtype: str) -> None:...
    
    def __init__(self, *args, **kwargs) -> None:
        
        _type = kwargs.get("_type")
        _subtype = kwargs.get("_subtype")

        self._type = _type
        self._subtype = _subtype
        self._extensions = []

    def __eq__(self, __o: "MediaTypeType") -> bool:

        return str(self).lower() == str(__o).lower()

    def __str__(self) -> str:
        return f"{self._type}/{self._subtype}"


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
class MediaType:
    class Audio:

        __attr__ = ["Aac", "Midi", "XMidi", "Mpeg", "Ogg", "Opus"]

        @property
        @final
        def Aac(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "aac")

        @property
        @final
        def Midi(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "midi")

        @property
        @final
        def XMidi(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "x-midi")

        @property
        @final
        def Mpeg(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "mpeg")

        @property
        @final
        def Ogg(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "ogg")

        @property
        @final
        def Opus(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "opus")

        @property
        @final
        def Wav(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "wav")

        @property
        @final
        def Webm(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "webm")

        @property
        @final
        def A3gpp(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "3gpp")

        @property
        @final
        def A3gpp2(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Audio, "3gpp2")

    class Application:
        class Vnd:
            class OpenxmlformatsOfficedocument:
                @property
                @final
                def WordprocessingmlDocument(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application,
                        "vnd.openxmlformats-officedocument.wordprocessingml.document",
                    )

                @property
                @final
                def PresentationmlPresentation(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application,
                        "vnd.openxmlformats-officedocument.presentationml.presentation",
                    )

                @property
                @final
                def SpreadsheetmlSheet(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application,
                        "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )

            class Apple:
                @property
                @final
                def InstallerXml(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application, "vnd.apple.installer+xml"
                    )

            class Oasis:
                @property
                @final
                def OpendocumentPresentation(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application, "vnd.oasis.opendocument.presentation"
                    )

            class Mozilla:
                @property
                @final
                def XulXml(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application, "vnd.mozilla.xul+xml"
                    )

            class Amazon:
                @property
                @final
                def Ebook(self) -> MediaTypeObject:
                    return MediaTypeObject(
                        MediaTypeType.Application, "vnd.amazon.ebook"
                    )

            @property
            @final
            def MsPowerpoint(self) -> MediaTypeObject:
                return MediaTypeObject(MediaTypeType.Application, "vnd.ms-powerpoint")

            @property
            @final
            def MsExcel(self) -> MediaTypeObject:
                return MediaTypeObject(MediaTypeType.Application, "vnd.ms-excel")

            @property
            @final
            def MsFontobject(self) -> MediaTypeObject:
                return MediaTypeObject(MediaTypeType.Application, "vnd.ms-fontobject")

            @property
            @final
            def Rar(self) -> MediaTypeObject:
                return MediaTypeObject(MediaTypeType.Application, "vnd.rar")

            @property
            @final
            def Visio(self) -> MediaTypeObject:
                return MediaTypeObject(MediaTypeType.Application, "vnd.visio")

        XAbiword = MediaTypeObject(MediaTypeType.Application, "x-abiword")
        XFreearc = MediaTypeObject(MediaTypeType.Application, "x-freearc")
        OctetStream = MediaTypeObject(MediaTypeType.Application, "octet-stream")
        XBzip = MediaTypeObject(MediaTypeType.Application, "x-bzip")
        XBzip2 = MediaTypeObject(MediaTypeType.Application, "x-bzip2")
        XCdf = MediaTypeObject(MediaTypeType.Application, "x-cdf")
        XCsh = MediaTypeObject(MediaTypeType.Application, "x-csh")
        Msword = MediaTypeObject(MediaTypeType.Application, "msword")
        EpubZip = MediaTypeObject(MediaTypeType.Application, "epub+zip")
        Gzip = MediaTypeObject(MediaTypeType.Application, "gzip")
        Json = MediaTypeObject(MediaTypeType.Application, "json")
        LdJson = MediaTypeObject(MediaTypeType.Application, "ld+json")
        Ogg = MediaTypeObject(MediaTypeType.Application, "ogg")
        Pdf = MediaTypeObject(MediaTypeType.Application, "pdf")
        XHttpdPhp = MediaTypeObject(MediaTypeType.Application, "x-httpd-php")
        Rtf = MediaTypeObject(MediaTypeType.Application, "rtf")
        XSh = MediaTypeObject(MediaTypeType.Application, "x-sh")
        XTar = MediaTypeObject(MediaTypeType.Application, "x-tar")
        XhtmlXml = MediaTypeObject(MediaTypeType.Application, "xhtml+xml")
        Xml = MediaTypeObject(MediaTypeType.Application, "xml")
        Zip = MediaTypeObject(MediaTypeType.Application, "zip")
        X7zCompressed = MediaTypeObject(MediaTypeType.Application, "x-7z-compressed")

    class Image:
        class Vnd:
            class Microsoft:
                @property
                @final
                def Icon(self) -> MediaTypeObject:
                    return MediaTypeObject(MediaTypeType.Image, "vnd.microsoft.icon")

        Avif = MediaTypeObject(MediaTypeType.Image, "avif")
        Bmp = MediaTypeObject(MediaTypeType.Image, "bmp")
        Gif = MediaTypeObject(MediaTypeType.Image, "gif")
        Jpeg = MediaTypeObject(MediaTypeType.Image, "jpeg")
        Png = MediaTypeObject(MediaTypeType.Image, "png")
        SvgXml = MediaTypeObject(MediaTypeType.Image, "svg+xml")
        Tiff = MediaTypeObject(MediaTypeType.Image, "tiff")
        Webp = MediaTypeObject(MediaTypeType.Image, "webp")

    class Video:
        XMsvideo = MediaTypeObject(MediaTypeType.Video, "x-msvideo")
        Mp4 = MediaTypeObject(MediaTypeType.Video, "mp4")
        Mpeg = MediaTypeObject(MediaTypeType.Video, "mpeg")
        Ogg = MediaTypeObject(MediaTypeType.Video, "ogg")
        Mp2t = MediaTypeObject(MediaTypeType.Video, "mp2t")
        Webm = MediaTypeObject(MediaTypeType.Video, "webm")
        V3gpp = MediaTypeObject(MediaTypeType.Video, "3gpp")
        V3gpp2 = MediaTypeObject(MediaTypeType.Video, "3gpp2")

    class Text:
        Css = MediaTypeObject(MediaTypeType.Text, "css")
        Csv = MediaTypeObject(MediaTypeType.Text, "csv")
        Html = MediaTypeObject(MediaTypeType.Text, "html")
        Calendar = MediaTypeObject(MediaTypeType.Text, "calendar")
        Javascript = MediaTypeObject(MediaTypeType.Text, "javascript")
        Plain = MediaTypeObject(MediaTypeType.Text, "plain")
        Xml = MediaTypeObject(MediaTypeType.Text, "xml")

    class Font:
        @property
        @final
        def Otf(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Font, "otf")

        @property
        @final
        def Ttf(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Font, "ttf")

        @property
        @final
        def Woff(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Font, "woff")

        @property
        @final
        def Woff2(self) -> MediaTypeObject:
            return MediaTypeObject(MediaTypeType.Font, "woff2")

    @classmethod
    def FromExtensions(cls, ext: str) -> "MediaTypeObject":

        ext = ext.replace(".", "")

        for _type in __types__:
            if ext.casefold() in _type._extensions:
                return _type
        
        return MediaTypeObject()


__types__: List[MediaTypeObject] = [
    MediaType.Audio.A3gpp,
    MediaType.Audio.A3gpp2,
    MediaType.Audio.Aac,
    MediaType.Audio.Midi,
]
