import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip()

        try:
            if re.fullmatch(r"\d{1,2}/\d{1,2}/\d{1,4}", date):
                month_str, day_str, year_str = date.split("/")
                month = int(month_str)
                day = int(day_str)
                year = int(year_str)

            elif re.fullmatch(r"[A-Za-z]+ \d{1,2}, \d{1,4}", date):
                parts = re.split(r"[ ,]+", date)
                month_str, day_str, year_str = parts

                if month_str not in months:
                    raise ValueError("Invalid month name")

                month = months.index(month_str) + 1
                day = int(day_str)
                year = int(year_str)

            else:
                raise ValueError("Invalid structure")

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Out-of-range values")

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except Exception:
            pass

if __name__ == "__main__":
    main()
