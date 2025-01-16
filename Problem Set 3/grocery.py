def main() :
    dict = {}
    while True :
        try :
            item = input().upper()
            if item in dict :
                dict[item] += 1
            else :
                dict[item] = 1
        except EOFError :
            keys = list(dict.keys())
            keys.sort()
            sorted_dict = {i: dict[i] for i in keys}
            for i in sorted_dict :
                print(sorted_dict[i], i)
            break

main()
