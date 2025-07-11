from twttr import shorten


def main():
    test_upper_lower()
    test_numbers()
    test_punctuation()

def test_upper_lower() :
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_numbers() :
    assert shorten('1234') == '1234'
    assert shorten('1234P') == '1234P'
    assert shorten('1234p') == '1234p'
    assert shorten('1234U') == '1234'
    assert shorten('1234u') == '1234'

def test_punctuation() :
    assert shorten(',;:!?.') == ',;:!?.'

if __name__ == "__main__":
    main()
