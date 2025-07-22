def main():
    while True:
        try:
            x,y = input("Fraction: ").strip().replace(" ", "").split("/")
            x,y = int(x), int(y)
            result = round(x / y, 2)

            if result <= 1 and x >= 0:
                percent = int(result*100)
                if percent >= 99:
                    print("F")
                elif percent <= 1:
                    print("E")
                else:
                    print(f"{percent}%")
                break
            else:
                pass

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
