from random import randint

while True:
    
    try:
        level = int(input('Level: ').strip())
        if level > 0:
            break
        
    except ValueError:
        pass

rand_num = randint(1, level)

while True:
    
    try:
        input_num = int(input('Guess: '))
        if input_num > rand_num:
            print('Too large!')

        
        elif input_num < rand_num:
            print('Too small!')

        else:
            print('Just right!')
            break
        
    except ValueError:
        pass
