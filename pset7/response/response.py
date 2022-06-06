from validators import email as is_email


def main():
    print('Valid' if is_email(input('Email address: ')) else 'Invalid')


if __name__ == '__main__':
    main()
