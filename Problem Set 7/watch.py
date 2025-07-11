import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'src="(.*?)\/embed(.*?)"', s) :
        link = re.search(r'(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)', s)
        if link :
            shorturl = link.groups()
            return "https://youtu.be/" + shorturl[3]







if __name__ == "__main__":
    main()
