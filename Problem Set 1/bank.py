def main():
    greet = input("Bank's greeting: ")
    due = greeting(greet)
    print(f"${due}")

def greeting(greet):
    greet = greet.lower().strip()
    if 'hello' in greet:
        return 0
    elif greet[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
