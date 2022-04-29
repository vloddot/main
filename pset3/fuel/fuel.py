while True:
    try:

        fraction = input('Fraction: ')
        x, y = fraction.split('/')

        x, y = float(x), float(y)

        result = float(x / y * 100)

        if x % 1 != 0 or y % 1 != 0:
            raise ValueError

        elif result > 100:
            raise ValueError

        elif result > 99:
            print('F')

        elif result < 1:
            print('E')

        else:
            print(f'{int(result)}%')

        break

    except (ValueError, ZeroDivisionError):
        pass