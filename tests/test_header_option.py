from pyrestsdk.type.model import HeaderOption

def test_header_option_init():
    header_option = HeaderOption("Authorization", "Bearer TOKEN")
    assert header_option.name == "Authorization"
    assert header_option.value == "Bearer TOKEN"
    assert str(header_option) == "Authorization:Bearer TOKEN"

def test_header_option_equality():
    header_option_1 = HeaderOption("Authorization", "Bearer TOKEN")
    header_option_2 = HeaderOption("Authorization", "Bearer TOKEN")
    assert header_option_1 == header_option_2

def test_header_option_inequality():
    header_option_1 = HeaderOption("Authorization", "Bearer TOKEN")
    header_option_2 = HeaderOption("Authorization", "Bearer OTHER_TOKEN")
    assert header_option_1 != header_option_2

def test_header_option_str():
    header_option = HeaderOption("Authorization", "Bearer TOKEN")
    assert str(header_option) == "Authorization:Bearer TOKEN"
