def main():
    message = input("Input: ")
    message_no_vow = shorten(message)
    print("Output : " + message_no_vow)

def shorten(word):
    no_vow = ""
    for letter in word :
        if not letter.lower() in ["a", "e", "i", "o", "u"] :
            no_vow += letter
    return no_vow

if __name__ == "__main__":
    main()

