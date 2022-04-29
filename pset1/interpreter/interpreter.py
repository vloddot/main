import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def main():

    expression = input('Expression: ').strip()

    counter = 0
    for operation in operations:
        try:
            index = expression.index(operation)
        except ValueError:
            counter += 1

        if counter == len(operations):
            try:
                print(int(expression.strip()))

            except ValueError:
                raise SyntaxError('Invalid syntax')

    try:
        x = float(expression[:index])
        operation = expression[index]
        y = float(expression[index + 1:])

        if x % 1 == 0 and y % 1 == 0:
            x = int(x)
            y = int(y)

    except ValueError:
        raise SyntaxError('Invalid syntax')

    try:
        print(operations[operation](x, y))

    except (ValueError, ZeroDivisionError):
        raise ValueError('Invalid operation')

    except KeyError:
        raise SyntaxError('Invalid syntax')


if __name__ == '__main__':
    main()
