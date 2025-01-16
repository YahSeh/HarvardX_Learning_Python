import operator

def main() :
    ops = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
    }
    n = input("Enter a simple aritmetic expression of two numbers :")
    x,y,z = n.split(" ")
    print(float(ops[y](int(x),int(z))))

main()
