price = 50

while price > 0:
    
    coins = int(input('Insert Coin: '))
    if coins != 25 and coins != 10 and coins != 5:
        print(f'Amount due: {price}')

    elif price < coins:
        print(f'Change owed: {coins - price}')
        break

    else:
        price -= coins
        print(f'Amount due: {price}')