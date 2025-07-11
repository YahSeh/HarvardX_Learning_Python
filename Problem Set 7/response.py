#import re
import validators
#import sys


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    #if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", s)
    valid = validators.email(s)
    if valid == True :
        return 'Valid'
    else :
        return 'Invalid'

if __name__ == "__main__":
    main()
