def main():
    fraction = input('Fraction: ').strip()
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction: str) -> int:
    x, y = fraction.split('/')
    x, y = float(x), float(y)

    if x % 1 != 0 or y % 1 != 0:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    result = (x / y) * 100

    if result > 100:
        raise ValueError

    return int(result)


def gauge(percentage: int) -> str:

    if percentage >= 99:
        return 'F'

    elif percentage <= 1:
        return 'E'

    else:
        return f'{percentage}%'


if __name__ == '__main__':
    main()
