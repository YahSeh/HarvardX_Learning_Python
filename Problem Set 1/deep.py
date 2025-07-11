import re

def main():
    pattern = r'^\s*(42|forty[- ]two)\s*$'
    inpt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if re.fullmatch(pattern, inpt, re.IGNORECASE) is not None:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
