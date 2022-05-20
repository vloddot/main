from sys import argv, exit


def main():

    if len(argv) != 2:
        print(f'Usage: python3 {argv[0]} file')
        exit(1)

    lines = 0

    if not argv[1].endswith('.py'):
        print('Use a python file.')
        exit(2)

    try:
        with open(argv[1]) as file:

            for line in file.readlines():
                if line.lstrip().startswith('#'):
                    continue

                if line.strip() == '':
                    continue

                lines += 1

    except FileNotFoundError:
        print('File not found.')
        exit(3)

    print(lines)


if __name__ == '__main__':
    main()
