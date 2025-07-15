def main():
    due = 50
    allowed = [25, 10, 5]

    while due > 0:
        print(f"Amount due: {due}")
        insert = int(input("Insert Coin: "))
        if insert in allowed:
            due = due - insert
        else:
            print("Wrong coin. Coins accepted: 25 cents, 10 cents, 5 cents.")

    print(f"Change Owed: {due * (-1)}") # Print a positive number, since the change owed is either < 0 or = 0


if __name__ == "__main__":
    main()
