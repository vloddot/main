def main():

    time = input('What time is it? ').strip()

    time = convert(time)

    if 18 <= time <= 19:
        print('dinner time')

    elif 12 <= time <= 13:
        print('lunch time')

    elif 7 <= time <= 8:
        print('breakfast time')


def convert(time):
    
    index = time.index(':')
    
    hour = int(time[:index])
    minute = int(time[index + 1:])
    
    float_hours = hour + minute / 60

    return float_hours


main()
