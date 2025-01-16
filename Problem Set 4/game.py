import random

while True :
    try :
        lvl = int(input("Level : "))
        if lvl > 0 :
            break
    except :
        pass

rand = random.randint(1, lvl)

while True :
    try :
        guess = int(input("Guess :"))
        if guess > 0 :
            if guess > rand :
                print("Too large!")
            elif guess < rand :
                print("Too small!")
            else:
                print("Just right!")
                break
    except :
        pass

'''

def main() :
    while True :
        try :
            lvl = int(input("Level : "))
            if lvl > 0 :
                break
        except :
            pass

    rand = random.randint(1, lvl)

    while True :
        try :
            guess = int(input("Guess :"))
            if guess > 0 :
                if guess > rand :
                    print("Too large!")
                elif guess < rand :
                    print("Too small!")
                else:
                    print("Just right!")
                    break
        except :
            pass


main()
'''
