import re
import pytest
from seasons import check_date

def main() :
    test_format()


def test_format() :
    assert check_date('2023-07-04') == ('2023', '07', '04')
    assert check_date('2023-7-2') == None
    assert check_date('July 3, 2023') == None



if __name__ == "__main__" :
    main()
