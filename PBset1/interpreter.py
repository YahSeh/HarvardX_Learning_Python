import operator

def main():
    expression = input("Expression: ")
    x, y, z = expression.split( " ")
    ope = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
    }

    print(float(ope[y](int(x), int(z))))


if __name__ == "__main__":
    main()
