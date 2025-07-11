import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #inpt = re.search(r"^(([1-9]|1[0-2]?)(:)*([0-5][0-9])* ([A,P]M) to ([1-9]|1[0-2]?)(:)*)([0-5][0-9])* ([A,P]M)", s)
    inpt = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([AP]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([AP]M)$", s)
    if inpt :
        grps = inpt.groups()
        if int(grps[1]) > 12 or int(grps[5]) > 12 :
            raise ValueError
        begin = format(grps[1], grps[2], grps[3])
        end = format(grps[5], grps[6], grps[7])
        return begin + ' to ' + end
    else :
        raise ValueError


def format(hour, minute, am_pm) :
    if am_pm == 'PM' :
        if int(hour) == 12 :
            new_hour = 12
        else :
            new_hour = int(hour) + 12
    else :
        if int(hour) == 12 :
            new_hour = 0
        else :
            new_hour = int(hour)
    if minute == None :
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else :
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time

if __name__ == "__main__":
    main()


