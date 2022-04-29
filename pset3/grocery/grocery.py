grocery_list = {}

while True:
    try:
        food = input().strip()

        if food in grocery_list:
            grocery_list[food] += 1

        else:
            grocery_list[food] = 1

    except EOFError:
        for key, value in sorted(grocery_list.items()):

            print(value, key.upper())

        break
