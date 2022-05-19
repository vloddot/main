from sys import argv, exit
import requests

if len(argv) != 2:
    print(f'Missing command line argument: python3 {argv[0]} bitcoin')
    exit(1)

try:
    bitcoin = float(argv[1])

except ValueError:
    print('Command line argument is not a number: python3 {argv[0]} bitcoin')
    exit(1)
    
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bitcoin_price = r.json()['bpi']['USD']['rate_float']
    print(f'${bitcoin_price * bitcoin:,.4f}')

except requests.RequestException:
    print('Could not find value of Bitcoin')
    exit(1)
