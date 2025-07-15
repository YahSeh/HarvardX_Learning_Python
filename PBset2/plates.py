import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    pattern = r'^[A-Z]{2}[A-Z]*[1-9][0-9]*$|^[A-Z]{2,6}$'
    return bool(re.fullmatch(pattern, plate))


if __name__ == "__main__":
    main()
