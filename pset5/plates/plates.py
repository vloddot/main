def main():
    plate = input('Plate: ')
    print('Valid') if is_valid(plate) else print('Invalid')


def is_valid(plate):
    
    if len(plate) > 6 or len(plate) < 2:
        return False

    if plate.isalpha():
        return True

    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    already_has_digit = False
    is_digit = False
    for char in plate:

        if char.isdigit() and not already_has_digit:
            is_digit = True
            already_has_digit = True

        if is_digit and char == '0':
            return False

        if is_digit and char.isalpha():
            return False
        
        is_digit = False

    return True


if __name__ == '__main__':
    main()
