def main():
    time = input("What time is it? ")
    converted = convert(time)
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")

def convert(time):
    time.replace(".", "")           # Takes into account either "a.m.", "am", "p.m." and "pm" as input
    hrs, min = time.split(":")

    if "pm" in time and 1 <= int(hrs) <= 12:
        hrs = int(hrs) + 12

    result = float(int(hrs)+round((int(min[:2])/60), 2))    # min[:2] to only take the numeral value of the element "min" which can be formatted as "## am" or "## pm"
    return result

if __name__ == "__main__":
    main()
