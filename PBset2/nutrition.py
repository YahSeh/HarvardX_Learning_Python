def main():
    dict = {
        "apple":            130,
        "avocado":          50,
        "banana":           110,
        "cantaloupe":       50,
        "grapefruits":      60,
        "honey dew":        50,
        "kiwifruit":        90,
        "lemon":            15,
        "lime":             20,
        "nectarine":        60,
        "orange":           80,
        "peach":            60,
        "pear":             100,
        "pineapple":        50,
        "plums":            70,
        "strawberries":     50,
        "sweet cherries":   100,
        "tangerine":        50,
        "watermelon":       80,
    }

    item = input("Item: ").lower()
    if item in dict:
        print(dict[item])

if __name__ == "__main__":
    main()
