import sys
import csv
from tabulate import tabulate

def main() :
    try :
        if len(sys.argv) == 3 :
            name, ext = str(sys.argv[1]).split(".")
            name2, ext2 = str(sys.argv[2]).split(".")
            if not ext == "csv" and not ext2 == "csv" :
                sys.exit("Not a CSV file")
            else :
                with open(sys.argv[1], "r") as file :
                    reader = csv.DictReader(file)
                    with open(sys.argv[2], "w", newline='') as new_file :
                        fieldnames = ['first', 'last', 'house']
                        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                        writer.writeheader()
                        for n in reader :
                            names = n['name'].split(",")
                            house = n['house']
                            writer.writerow({'first': names[1].lstrip(), 'last': names[0].strip(), 'house': house})

        elif len(sys.argv) < 3 :
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 3 :
            sys.exit("Too many command-line arguments")

    except FileNotFoundError :
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
