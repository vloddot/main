from re import sub, IGNORECASE

text = input('Input: ')

text = sub(r'(a|e|i|o|u)', '', text, flags=IGNORECASE)

print(f'Output: {text}')