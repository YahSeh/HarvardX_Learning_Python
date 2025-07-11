def main() :
    due = 50
    den = [25, 10, 5]
    while due > 0 :
        ins = int(input("Insert coin: "))
        if ins in den :
            due = (due-ins)
            if due > 0:
                print(f"Amount Due: {due}\n")
        else :
            #print("We only accept coins of 25 cents, 10 cents or 5 cents.")
            print(f"Amount Due: {due}\n")
    print(f"Change Owed: {(due*(-1))}")

main()
