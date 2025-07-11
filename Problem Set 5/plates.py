def main():
    plate = input("Plate: ")
    if is_valid(plate) == True :
        print("Valid")
    else :
        print("Invalid")

def is_valid(s):
    s = s.upper()   #capitalize input
    #checks length of plate is between 2 and 6 characters
    if (len(s) < 2) or (len(s) > 6) :
        return False

    #checks if te first two characters are letters
    if s[0].isalpha() == False or s[1].isalpha() == False :
        return False

    #checks if there are numerical characters, and return False if the first one is a zero
    i = 0
    while i < len(s) :
        if s[i].isalpha() == False :
            if s[i] == "0":
                return False
            elif s[i:].isdigit() == False :
                return False
            else:
                return True
        i += 1

    #
    return True
'''
def is_valid(s):
    s = s.upper()   #capitalize input
    if (len(s) <= 6) and (len(s) >= 2) and (s[0:2].isalpha()) : #check size and if first 2 characters are letters
        if any(i.isdigit() for i in s) :                        #check if the input has any number
            dig = [int(i) for i in s if i.isdigit()]            #creates a list that contains all the numbers found in the input
            for i in range(2, len(s)):                          #checks each character after the first two in the input
                if s[i].isdigit() and (dig[0] != 0):            #checks if the character is a number and if the first number in the input isn't a zero
                    if s[i:].isdigit() :                        #if the rest of the character after this one are ALL numbers, return True
                        return True
                    else:                       #if there is a letter amongst the rest of the characters after the first number found, return False
                        return False
                else :
                    return False
        elif s.isalpha() :         #if there is no number in the input, return True (while it meets the size requierments)
            return True
        else :
            return False
    else :
        return False

if __name__ == "__main__":
    main()


def is_valid(s):
    s = s.upper()   #capitalize input
    if (len(s) <= 6) and (len(s) >= 2) and (s[0:2].isalpha()) : #check size and if first 2 characters are letters
        if any(i.isdigit() for i in s) :          #check if the input has any number
            if s[i].rfind()
        elif not any(str(i).isdigit() for i in s) :
            return True
    else :
        return False
'''

'''

                for i in range(2, len(s)) :
                    print(i)
                    if s[i].isdigit() and i == 2:
                        i += 1
                    elif not s[i].isdigit() :
                        i += 1
                    elif i > 2 and s[(i-1)].isalpha() and s[(i-1)].isalpha() :
                        i +1
'''
