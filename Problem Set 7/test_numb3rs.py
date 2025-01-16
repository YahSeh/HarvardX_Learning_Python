import re
from numb3rs import validate

def main() :
    test_length()
    test_number()
    test_variable()

def test_length() :
    assert validate(r'192.168.2.1') == True
    assert validate(r'192.168.2.1.0') == False
    assert validate(r'192.168.1') == False
    assert validate(r'192.168') == False
    assert validate(r'192') == False

def test_number() :
    assert validate(r'255.0.255.1') == True
    assert validate(r'888.255.255.255') == False
    assert validate(r'255.888.255.255') == False
    assert validate(r'255.255.888.255') == False
    assert validate(r'255.255.255.888') == False
    assert validate(r'-1.-1.-1.-1') == False

def test_variable() :
    assert validate(r'cat.dog.cat.dog') == False

if __name__ == "__main__":
    main()
