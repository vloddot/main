greeting = input('Greeting: ').strip()

# If the first 5 letters of the greeting are hello no matter what case the user types in, print $0
if greeting.upper()[:5] == 'HELLO':
    
    print('$0')
    
# If the first letter of the greeting is an h no matter what case the user types in, print $20
elif greeting[0].upper() == 'H':
    
    print('$20')
    
# Else, base case. $100
else:
    print('$100')