import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip) :
        ls = ip.split(".")
        for nb in ls :
            if int(nb) < 0 or int(nb) > 255 :
                return False
        return True
    else :
        return False


if __name__ == "__main__":
    main()


#^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$
#^\d+\.\d+\.\d+\.\d+$
