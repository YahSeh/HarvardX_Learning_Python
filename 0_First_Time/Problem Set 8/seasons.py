import sys
import re
import inflect
#import datetime
#import operator
from datetime import date

p = inflect.engine()

def main():
    birthdate = input("Date of Birth: ")
    try :
        y, m, d = check_date(birthdate)
    except :
        sys.exit("Invalid date")
    birth = date(int(y), int(m), int(d))
    today = date.today()
    diff = today - birth
    minutes = diff.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize() + " minutes")

def check_date(birthdate) :
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthdate) :
        y, m, d = birthdate.split("-")
        return y, m, d


if __name__ == "__main__":
    main()
