from PIL import Image, ImageOps, UnidentifiedImageError
from sys import argv, exit
from os import path

def main():
    if len(argv) != 3:
        print(f'Usage: python3 {argv[0]} infile outfile')
        exit(1)

    if not (
        (path.splitext(argv[1])[1] == '.png' and path.splitext(argv[2])[1] == '.png') or
        (path.splitext(argv[1])[1] == '.jpg' and path.splitext(argv[2])[1] == '.jpg')
    ):
        print('Use a JPG/JPEG or PNG image.')
        exit(2)

    try:
        with Image.open(argv[1]) as in_image:
            with Image.open('shirt.png') as shirt:
                in_image = ImageOps.fit(
                    in_image, shirt.size
                )

                in_image.paste(shirt, shirt)
                in_image.save(argv[2])

    except (FileNotFoundError, UnidentifiedImageError) as exc:
        print(exc)
        exit(3)


if __name__ == '__main__':
    main()
