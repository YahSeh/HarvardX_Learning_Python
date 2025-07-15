import re

def main():
    inpt = input("Input: ")
    print(re.sub(r'[AaEeIiOoUu]', '', inpt))


if __name__ == "__main__":
    main()
