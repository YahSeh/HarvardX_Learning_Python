import sys

def main() :
    try :
        if len(sys.argv) == 2 :
            name, ext = str(sys.argv[1]).split(".")
            if not ext == "py" :
                sys.exit("Not a Python file")
            else :
                with open(str(sys.argv[1]), "r") as file :
                    count = 0
                    for line in file :
                        if not line.lstrip().startswith("#") and not line.isspace() :
                            count += 1
                print(count)

        elif len(sys.argv) < 2 :
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 2 :
            sys.exit("Too many command-line arguments")

    except FileNotFoundError :
        sys.exit("File does not exist")

main()
