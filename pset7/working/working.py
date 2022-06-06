from re import findall


def main():
    print(convert(input('Hours: ')))


def convert(s):
    regex = findall(
        r'^(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) (to) (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)$', s
    )

    if not regex:
        raise ValueError

    regex = regex[0]

    hours = [regex[0], regex[4]]
    minutes = [regex[1], regex[5]]
    post_meridiems = [regex[2] == 'PM', regex[6] == 'PM']

    orig_hours = hours
    ret = ""
    for hour, orig_hour, minute, post_meridiem in zip(hours, orig_hours, minutes, post_meridiems):

        if post_meridiem:
            if hour == '12':
                pass
            else:
                hour = int(hour)
                hour += 12
                hour %= 24
                hour = str(hour)

        elif hour == '12':
            hour = '0'

        if hour < orig_hour:
            post_meridiem = False

        ret += '{0}{1} to '.format("%02d" % int(hour),
                                   f':{minute}' if minute else ':00',
                                   'PM' if post_meridiem else 'AM')

    return ret[:-3]


if __name__ == '__main__':
    main()
