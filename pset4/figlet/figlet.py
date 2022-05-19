from random import choice
from sys import argv, exit
from pyfiglet import Figlet

figlet = Figlet()
if len(argv) != 1 and len(argv) != 3:
    print(f'Usage: python {argv[0]} [--font|-f (font)]')
    exit(1)

fonts = figlet.getFonts()

if len(argv) == 3:
    if argv[1] != '-f' and argv[1] != '--font':
        print(f'Usage: python {argv[0]} [--font|-f (font)]')
        exit(1)
        
if argv[2] not in fonts:
     print('Invalid font')
     exit(1)
        
text = input('Input: ').strip()

if len(argv) == 1:
    font = choice(fonts)
    figlet.setFont(font=font)
    print(f'Output: \n{figlet.renderText(text)}')

elif (argv[1] == '-f' or argv[1] == '--font'):

        font = argv[2]
        figlet.setFont(font=font)
        print(f'Output: \n\n\n{figlet.renderText(text)}')

else:
    print(f'Usage: python {argv[0]} [--font|-f (font)]')
    exit(1)
