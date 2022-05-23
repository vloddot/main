from re import sub

camelCase = input('camelCase: ')

snake_case = [sub(r'[A-Z]', f'_{char.lower()}', char) for char in camelCase]

print('snake_case: ', end="")

for char in snake_case:
    print(char, end="")
    
print()