from tabulate import tabulate
from sys import argv, exit
import csv

def main():
    if len(argv) != 2:
        print(f'Usage: python3 {argv[0]} csvfile')
        exit(1)

    if not argv[1].endswith('.csv'):
        print('Use a csv file.')

    try:
        with open(argv[1]) as file:
            reader = csv.reader(file)
            print(tabulate(reader))

    except FileNotFoundError:
        print('File not found.')
        exit(2)


if __name__ == '__main__':
    main()
