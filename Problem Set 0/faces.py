def main():
    inpt = input("Enter a phrase with a smiley face (e.g., 'Hello World :)':\n").replace(":)", "🙂").replace(":(", "🙁")

    print(inpt)

if __name__ == "__main__":
    main()
