from re import findall, IGNORECASE


def main():
    print(parse(input('HTML: ')))


def parse(s):
    regex = findall(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)(\.)(com|be)(/)embed/(.{11})', s, IGNORECASE)

    if regex:
        return f'https://youtu.be/{regex[0][-1:][0]}'


if __name__ == '__main__':
    main()
