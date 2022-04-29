prices = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

items = {}

while True:
    try:
        item = input('Item: ').title().strip()
    
    except EOFError:
        break

    if item in prices:
        if item in items:
            items[item] += prices[item]

        else:
            items[item] = prices[item]
            
        
        print(f'Total: ${sum(items.values()):.2f}')