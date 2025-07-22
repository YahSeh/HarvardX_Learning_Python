def main():
    dict = {}

    while True:
        try:
            item = input("").upper()
            if item in dict:
                dict[item] += 1
            else:
                dict.update({item : 1})

        except KeyError:
            print("Key error")
            pass

        except EOFError:
            print("\n")
            for i in sorted(dict):
                print(dict[i], i)
            break



if __name__ == "__main__":
    main()
