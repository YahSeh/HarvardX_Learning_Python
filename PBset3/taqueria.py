def main():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0

    while True:
        try:
            order = input("Item: ").title().strip()
            if order in dict:
                total += dict[order]
                print(f"Total: $%.2f" % total)
            else:
                pass
        except EOFError:
            break


if __name__ == "__main__":
    main()
