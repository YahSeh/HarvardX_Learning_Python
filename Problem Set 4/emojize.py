import emoji

def main() :
    txt = str(input("Input : "))
    print("Output :", emoji.emojize(txt, language='alias'))

main()
