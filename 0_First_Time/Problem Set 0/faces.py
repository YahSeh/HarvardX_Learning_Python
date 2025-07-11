
def main() :
    phrase = str(input("Say something with an emoji :\n"))
    phrase = convert(phrase)
    print(phrase)

def convert(phrase) :
    #phrase = phrase.replace(":)", "🙂")
    #phrase = phrase.replace(":(", "🙁")
    phrase = phrase.replace(":)", "🙂").replace(":(", "🙁")
    return phrase

main()
