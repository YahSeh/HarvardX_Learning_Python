import re

def main():
    d_pattern = r'^\$\d+\.\d{2}$'
    p_pattern = r'^\d+%$'
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")

    while True:
        if re.fullmatch(d_pattern, dollars) and re.fullmatch(p_pattern, percent):
            dollars_float = dollars_to_float(dollars)
            dollars_percent = percent_to_float(percent)

            tip = dollars_float * dollars_percent
            print(f"Leave ${tip:.2f}")
            return

        else:
            print("Invalid format, please enter the right format (e.g., $50.00 and 15%).")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100


if __name__ == "__main__":
    main()
