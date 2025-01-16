def main() :
    vow = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    inp = str(input("Input: "))
    for i in inp :
        if i in vow :
            inp = inp.replace(i, "")
    print(f"Output : {inp}")

main()
