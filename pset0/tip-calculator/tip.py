def main():

    # Take dollar input from the user and convert it to a float
    dollars = dollars_to_float(input('How much was the meal? '))
    
    # Take percentage input from the user and convert it to a float
    percent = percent_to_float(input('What percentage would you like to tip? '))

    # Calculate the tip
    tip = dollars * percent

    # Print the tip
    print(f'Leave ${tip:.2f}')


def dollars_to_float(dollars):
    
    # Return a float of the dollars from the start of the second character in the string
    # because the user will type something like $50.00
    return float(dollars[1:])


def percent_to_float(percent):
    
    # Return a float of the percentage from the start to the length of the percentage - 1
    # because the user will type something like 15% then divide it by 100 to make it 0.15
    return float(percent[:len(percent) - 1]) / 100


main()