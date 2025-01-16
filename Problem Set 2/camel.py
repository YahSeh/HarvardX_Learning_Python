def main():
    name = str(input("camelCase: "))
    for i in name :
        if i.isupper() == True :
            name = name.replace(i, (f"_{i}"))
    name = name.lower()
    print(f"snake_case: {name}")
    return

main()
