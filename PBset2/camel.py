import re

def main():
    var = input("Camel case: ")
    print(re.sub(r'(?<!^)(?=[A-Z])', '_', var).lower())


if __name__ == "__main__":
    main()
