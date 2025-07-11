def main() :
    n = input("What time is it ? ")
    time = convert(n)
    if 7 <= time <= 8 :
        print("breakfast time")
    elif 12 <= time <= 13 :
        print("lunch time")
    elif 18 <= time <= 19 :
        print("dinner time")


def convert(time) :
    hours, minutes = time.split(":")
    conv_hour = float(int(hours)+round((int(minutes)/60), 2))
    return conv_hour

if __name__ == "__main__":
    main()
