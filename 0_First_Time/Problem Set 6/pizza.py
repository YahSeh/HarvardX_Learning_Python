import sys
import csv
from tabulate import tabulate

def main() :
    try :
        if len(sys.argv) == 2 :
            name, ext = str(sys.argv[1]).split(".")
            if not ext == "csv" :
                sys.exit("Not a CSV file")
            else :
                with open(sys.argv[1], "r") as file :
                    reader = csv.reader(file)
                    ls = []
                    for n in reader :
                        ls.append(n)
                print(tabulate(ls[1:], headers=ls[0], tablefmt="grid"))

        elif len(sys.argv) < 2 :
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 2 :
            sys.exit("Too many command-line arguments")

    except FileNotFoundError :
        sys.exit("File does not exist")
'''


def main() :
    try :
        if len(sys.argv) == 2 :
            name, ext = str(sys.argv[1]).split(".")
            if not ext == "csv" :
                sys.exit("Not a CSV file")
            else :
                with open(str(sys.argv[1]), "r") as file :
                    first_line = file.readline().strip().split(",")
                    headers = file.readlines()
                    ls = []
                    for n in headers :
                        line = n.split(",")
                        ls.append(line)
                print(tabulate(ls, first_line, tablefmt="grid"))


        elif len(sys.argv) < 2 :
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 2 :
            sys.exit("Too many command-line arguments")

    except FileNotFoundError :
        sys.exit("File does not exist")
'''
main()
