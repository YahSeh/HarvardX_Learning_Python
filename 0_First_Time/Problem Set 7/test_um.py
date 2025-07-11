import re
import pytest
from um import count

def main() :
    test_capitalize()
    test_inword()
    test_sentence()

def test_capitalize() :
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_inword() :
    assert count('Album') == 0
    assert count('Yummy') == 0

def test_sentence() :
    assert count('Um?') == 1
    assert count('Hello um world') == 1
