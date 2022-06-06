from re import findall
from sys import exit


def check_binary(binary):
    return findall(r'([01])', binary)


# def read_binary(binary):
    


def write_binary(multiples, num):
    if '+' in binary:
        return binary.split('+')[0]
    elif '-' in binary:
        return perform_operation(binary.split('-'), '-')
    elif '*' in binary:
        return perform_operation(binary.split('*'), '*')
    elif '/' in binary:
        return perform_operation(binary.split('/'), '/')
    

    print(num)


def perform_operation(binary_nums, operation):
    pass

def main():
    binary = input('Binary: ').strip().replace(' ', '')
    if check_binary(binary):
        print('Invalid binary operation')
        exit(1)


    print(write_binary(multiples, num))


if __name__ == '__main__':
    main()
