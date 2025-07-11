import inflect

p = inflect.engine()

ls =[]

def main() :
    while True :
        try :
            names = str(input("Name : "))
            ls.append(names)
            all = p.join(ls)
        except EOFError :
            print(f"Adieu, adieu, to {all}")
            break

main()
