from re import match


def main():
    plate = input('Plate: ')
    print('Valid') if is_valid(plate) else print('Invalid')


def is_valid(plate: str) -> bool:
    # scratch this mess: return match(r'([A-Za-z]{2,6}([1-9][0-9])?|[A-Za-z]{2,6}){2,6}', plate)

    if len(plate) > 6 or len(plate) < 2:
        return False

    if plate.isalpha():
        return True

    if not plate[0:2].isalpha():
        return False

    if not match(r'^[0-9]*[^0-9]*[0-9]*$', plate):
        return False

    if match(r'^\w*0', plate):
        return False

    return True


if __name__ == '__main__':
    main()
