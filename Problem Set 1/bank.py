def main():
    greet = input("Greeting : ").lower().replace(" ", "")
    if "hello" in greet : # and greet[0] == "h" :
        print("$0")
    elif greet[0] == "h" and "hello" not in greet :
        print("$20")
    else :
        print("$100")
    return

main()
