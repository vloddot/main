import csv
from sys import argv, exit


def main():
    if len(argv) != 3:
        print(f'Usage: python3 {argv[0]} infile outfile')
        exit(1)

    if not argv[1].endswith('.csv'):
        print('Use a csv input file.')
        exit(2)

    if not argv[2].endswith('.csv'):
        argv[2] += '.csv'

    try:
        with open(argv[1], 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            last_names = []
            first_names = []
            houses = []
            for row in reader:
                split_tuple = row['name'].split(',')
                last_names.append(split_tuple[0])
                first_names.append(split_tuple[1])
                houses.append(row['house'])

    except FileNotFoundError:
        print('File not found.')
        exit(3)

    with open(argv[2], 'w', encoding="utf-8") as file:
        file.write('first,last,house\n')
        for first_name, last_name, house in zip(first_names, last_names, houses):
            file.write(f'{first_name},{last_name},{house}\n'.lstrip())


if __name__ == '__main__':
    main()
