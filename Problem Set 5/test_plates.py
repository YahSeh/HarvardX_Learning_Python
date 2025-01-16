from plates import is_valid

def main() :
    test_beginning()
    test_middle()
    test_zero()
    test_punctuation()
    test_length()

def test_length() :
    assert is_valid('AAAAAA') == True
    assert is_valid('A') == False
    assert is_valid('AAAAAAA') == False

def test_beginning() :
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('1A') == False
    assert is_valid('11') == False

def test_middle() :
    assert is_valid('AA1111') == True
    assert is_valid('AAAAAA') == True
    assert is_valid('AA1A') == False
    assert is_valid('AA1AA1') == False

def test_zero() :
    assert is_valid('AA10') == True
    assert is_valid('AA01') == False
    assert is_valid('AA001') == False
    assert is_valid('AA1010') == True

def test_punctuation() :
    assert is_valid('AA!') == False
    assert is_valid('AA.') == False
    assert is_valid('AA?') == False
    assert is_valid('AA,') == False
    assert is_valid("AA'") == False
    assert is_valid('AA A') == False
    assert is_valid('AA 1') == False
    assert is_valid('AA 0') == False

if __name__ == "__main__":
    main()
