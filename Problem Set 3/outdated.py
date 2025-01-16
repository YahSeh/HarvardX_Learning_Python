def main() :
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True :
        try :
            date = str(input("Date : ").capitalize())
            if "/" in date :
                n = date.split("/")
                if int(n[0]) > 12 or int(n[1]) > 31:
                    pass
                elif 1 <= int(n[0]) <= 12 :
                    m, d = int(n[0]), int(n[1])
                    print(f"{int(n[2])}-{m:02}-{d:02}")
                    break
            elif " " and "," in date :
                n = date.replace(",", "").split(" ")
                m, d = int(months.index(n[0])+1), int(n[1])
                if n[0] in months and int(n[1]) <= 31 :
                    print(f"{n[2]:02}-{m:02}-{d:02}")
                    break
                else :
                    pass
            else :
                pass
                #print("Wrong date format. Please use MM/DD/YYYY or Month DD, YYYY formats.")
        except ValueError :
            print("Date not found, try again")
            pass

main()
