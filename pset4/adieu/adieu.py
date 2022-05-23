from inflect import engine

p = engine()
try:
    names = ['hello', 'world']
    while True:
        name = input('Name: ').strip()
        names.append(name)

except EOFError:
    print(f'Adieu, adieu, to {p.join((names))}')
