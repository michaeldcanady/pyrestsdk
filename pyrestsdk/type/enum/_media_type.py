from strenum import LowercaseStrEnum
from enum import auto

class MediaTypeType(LowercaseStrEnum):
    
    Application = auto()
    Audio = auto()
    Image = auto()
    Text = auto()
    Video = auto()
    Font = auto()

class MediaTypeObject(object):
    
    def __init__(self, _type: MediaTypeType, _subtype: str) -> None:
        
        self._type = _type
        self._subtype = _subtype
        
    def __str__(self) -> str:
        return f"{self._type}/{self._subtype}"
    
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
class MediaType:
    class Audio:
        Aac = MediaTypeObject(MediaTypeType.Audio, "aac")
        Midi = MediaTypeObject(MediaTypeType.Audio, "midi")
        XMidi = MediaTypeObject(MediaTypeType.Audio, "x-midi")
        Mpeg = MediaTypeObject(MediaTypeType.Audio, "mpeg")
        Ogg = MediaTypeObject(MediaTypeType.Audio, "ogg")
        Opus = MediaTypeObject(MediaTypeType.Audio, "opus")
        Wav = MediaTypeObject(MediaTypeType.Audio, "wav")
        Webm = MediaTypeObject(MediaTypeType.Audio, "webm")
        A3gpp = MediaTypeObject(MediaTypeType.Audio, "3gpp")
        A3gpp2 = MediaTypeObject(MediaTypeType.Audio, "3gpp2")

    class Application:
        class Vnd:
            class OpenxmlformatsOfficedocument:
                WordprocessingmlDocument = MediaTypeObject(MediaTypeType.Application, "vnd.openxmlformats-officedocument.wordprocessingml.document")
                PresentationmlPresentation = MediaTypeObject(MediaTypeType.Application, "vnd.openxmlformats-officedocument.presentationml.presentation")
                SpreadsheetmlSheet = MediaTypeObject(MediaTypeType.Application, "vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            class Apple:
                InstallerXml = MediaTypeObject(MediaTypeType.Application, "vnd.apple.installer+xml")
            class Oasis:
                OpendocumentPresentation = MediaTypeObject(MediaTypeType.Application, "vnd.oasis.opendocument.presentation")
            class Mozilla:
                XulXml = MediaTypeObject(MediaTypeType.Application, "vnd.mozilla.xul+xml")  
            class Amazon:
                Ebook = MediaTypeObject(MediaTypeType.Application, "vnd.amazon.ebook")
            
            MsPowerpoint = MediaTypeObject(MediaTypeType.Application, "vnd.ms-powerpoint")
            MsExcel =  MediaTypeObject(MediaTypeType.Application, "vnd.ms-excel")
            MsFontobject = MediaTypeObject(MediaTypeType.Application, "vnd.ms-fontobject")
            Rar = MediaTypeObject(MediaTypeType.Application, "vnd.rar")
            Visio = MediaTypeObject(MediaTypeType.Application, "vnd.visio")
        
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
            MicrosoftIcon = MediaTypeObject(MediaTypeType.Image, "vnd.microsoft.icon")
            
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
        Otf = MediaTypeObject(MediaTypeType.Font, "otf")
        Ttf = MediaTypeObject(MediaTypeType.Font, "ttf")
        Woff = MediaTypeObject(MediaTypeType.Font, "woff")
        Woff2 = MediaTypeObject(MediaTypeType.Font, "woff2")