def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction: str) -> int:
    x, y = fraction.split('/')
    x, y = float(x), float(y)

    if x > y or x % 1 != 0 or y % 1 != 0:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    result = float(x / y * 100)

    if result > 100:
        raise ValueError

    return int(round(result))


def gauge(percentage: float) -> str:
    if percentage >= 99:
        return 'F'

    elif percentage <= 1:
        return 'E'

    else:
        return f'{percentage}%'


if __name__ == '__main__':
    main()
