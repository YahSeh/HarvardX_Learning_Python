def main():
    x = str((input("Fraction : ")))
    frac = convert(x)
    output = gauge(frac)
    print(output)


def convert(fraction):
    while True :
        try :
            num, denum = fraction.split("/")
            new_num = int(num)
            new_denum = int(denum)
            result = new_num / new_denum
            #result = (int((round((ls[0] / ls[1])*100,2))))
            #return result
            if result <= 1 :
                percent = int(result *100)
                return percent
            else :
                fraction = input("Fraction :")
                pass
        except (ValueError, ZeroDivisionError) :
            print("Fraction not valid.")
            raise



def gauge(percentage):
    if percentage <= 1 :
        return "E"
    elif percentage >= 99 :
        return "F"
    else :
        return str(percentage) + "%"


if __name__ == "__main__":
    main()


'''
def main():
    while True :
        try :
            x = (input("Fraction : "))
            ls = [int(i) for i in x.split("/")]
            print((round((ls[0] / ls[1])*100,2)),"%")
        except (ValueError, ZeroDivisionError) :
            print("Fraction not valid.")
        else :
            break


main()
'''
