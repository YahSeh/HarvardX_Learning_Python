def main ():
    deep = input("What is the Answer to the Great Qeustion of Life, the Universe, and Everything ?\n").lower()
    deep = deep.strip()
    if deep == "42" or deep == "forty-two" or deep == "forty two" :
        print("Yes")
    else :
        print("No")
    return

main()
