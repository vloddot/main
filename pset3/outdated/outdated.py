
from re import sub
from sys import exit

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input('Date: ').strip()

    date = date.split('/')

    if not date[0].isdigit() and len(date) == 1:
        date = date[0].split(' ')


        for i in range(len(date)):
            date[i] = sub(r'(,)|( )', '', date[i])

        try:
            if date[0] not in months:
                raise ValueError

            if int(date[1]) > 31:
                raise ValueError

            print(f'{date[2]}-{months[date[0]]:>02}-{date[1]:>02}')

        except ValueError:
            continue

        break

    try:
        if int(date[0]) > 12:
            raise ValueError

        if int(date[1]) > 31:
            raise ValueError

        print(f'{date[2]}-{date[0]:>02}-{date[1]:>02}')

        break

    except ValueError:
        continue
