expression = input('Expression: ').strip()

x, y, z = expression.split(' ')
x, z = int(x), int(z)

operations = {
    '+': lambda x, z: print(f'{x + z:.1f}'),
    '-': lambda x, z: print(f'{x - z:.1f}'),
    '/': lambda x, z: print(f'{x / z:.1f}'),
    '*': lambda x, z: print(f'{x * z:.1f}'),
}

operations[y](x, z)
