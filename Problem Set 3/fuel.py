def main():
    while True :
        try :
            fraction = str((input("Fraction : ")))
            num, denum = fraction.split("/")
            new_num = int(num)
            new_denum = int(denum)
            result = round(new_num / new_denum, 2)
            if result <= 1 :
                percent = int(result *100)
                if percent <= 1 :
                    print("E")
                elif percent >= 99 :
                    print("F")
                else :
                    print(str(percent) + "%")
                break
            elif result > 1 :
                fraction = str((input("Fraction : ")))
        except (ValueError, ZeroDivisionError) :
            #print("Fraction not valid.")
            pass


main()
