def main():
<<<<<<< HEAD
    fraction = input('Fraction: ').strip()
=======
    fraction = input('Fraction: ')
>>>>>>> 3789f49be75645444e2f8be47c551d8abac42471
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction: str) -> int:
    x, y = fraction.split('/')
    x, y = float(x), float(y)

<<<<<<< HEAD
    if x % 1 != 0 or y % 1 != 0:
=======
    if x > y or x % 1 != 0 or y % 1 != 0:
>>>>>>> 3789f49be75645444e2f8be47c551d8abac42471
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

<<<<<<< HEAD
    if x > y:
        raise ValueError

    result = (x / y) * 100
=======
    result = float(x / y * 100)
>>>>>>> 3789f49be75645444e2f8be47c551d8abac42471

    if result > 100:
        raise ValueError

<<<<<<< HEAD
    return int(result)


def gauge(percentage: int) -> str:

=======
    return int(round(result))


def gauge(percentage: float) -> str:
>>>>>>> 3789f49be75645444e2f8be47c551d8abac42471
    if percentage >= 99:
        return 'F'

    elif percentage <= 1:
        return 'E'

    else:
        return f'{percentage}%'


if __name__ == '__main__':
    main()
