from PIL import Image, ImageOps
from sys import argv, exit


def main():
    if len(argv) != 3:
        print(f'Usage: python3 {argv[0]}')
        exit(1)

    if not ((argv[1].endswith('.jpg') or argv[1].endswith('.jpeg') and (argv[1].endswith('.jpg') or argv[1].endswith('.jpeg')))):
        if not (argv[1].endswith('.png') and argv[2].endswith('.png')):
            print('Use a jpg/jpeg or png file.')

    with Image.open(argv[1]) as image:
        ImageOps.fit(image)


if __name__ == '__main__':
    main()
