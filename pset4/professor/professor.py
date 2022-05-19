from random import randint

def main():
    
    level = get_level()
    

    for _ in range(10):

        x, y = generate_integer(level)

        wrong_answers = 0        
        while True:
            if wrong_answers >= 3:
                print(f'{x} + {y} = {x + y}')
                break

            try:
                answer = int(input(f'{x} + {y} = '))
                if x + y != answer:
                    raise ValueError
                else:
                    break

            except ValueError:
                print('EEE')
                wrong_answers += 1



def get_level():

    while True:
        try:
            n = int(input('Level: ').strip())
            if n in [1, 2, 3]:
                break

        except ValueError:
            pass
        
    return n


def generate_integer(level):

    # Generate random numbers and the 'level' is just
    # how many digits are in the integer
    
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
        return x, y

    x = randint(10 ** (level - 1), (10 ** level) - 1)
    y = randint(10 ** (level - 1), (10 ** level) - 1)
    return x, y                
    





if __name__ == '__main__':
    main()
