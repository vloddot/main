from re import match


def main():
    print(validate(input('IPV4 Address: ')))


def validate(ip):
    return True if match(r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}', ip) else False


if __name__ == '__main__':
    main()
