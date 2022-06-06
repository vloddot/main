from datetime import date
from sys import exit
from inflect import engine


def main():
    engn = engine()
    birth_date = get_date()
    age_in_minutes = calculate_age_in_minutes(birth_date)

    print(f'{engn.number_to_words(age_in_minutes, andword="").capitalize()} minutes')


def calculate_age_in_minutes(birth_date):
    age_in_minutes = ((date.today() - birth_date).days * 24 *
                      60 + (date.today() - birth_date).seconds // 60)

    return age_in_minutes


def get_date():
    try:
        birth_date = date.fromisoformat(input('Enter a date: '))
    except ValueError:
        print('Use YYYY-MM-DD format')
        exit(1)

    return birth_date


if __name__ == '__main__':
    main()
