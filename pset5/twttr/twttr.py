from re import sub, IGNORECASE


def main():
    text = input('Text: ').strip()
    print(shorten(text))


def shorten(word):
    return sub(r'(a|e|i|o|u)', '', word, flags=IGNORECASE)


if __name__ == '__main__':
    main()
