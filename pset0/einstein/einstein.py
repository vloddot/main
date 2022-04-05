import sys

# Ask for the input of m and if the conversion to int failed go into the except statement
try:
    m = int(input('m: ').strip())
except ValueError:
    print('Invalid value for m')
    sys.exit(1)
    
# Print the energy using the famous formula: E = mc squared
print(f"E: {int(m * (300000000 * 300000000))}")