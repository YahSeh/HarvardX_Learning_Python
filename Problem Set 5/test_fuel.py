from fuel import convert, gauge
import pytest

def main() :
    test_capacity()
    test_zerodiv()
    test_value()

def test_capacity() :
    assert convert('50/100') == 50 and gauge(50) == '50%'
    assert convert('1/2') == 50 and gauge(50) == '50%'
    assert convert('1/3') == 33 and gauge(33) == '33%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

def test_zerodiv() :
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value() :
    with pytest.raises(ValueError) :
        convert('a/b')

if __name__ == "__main__":
    main()
