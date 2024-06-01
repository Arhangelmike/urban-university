import math


def divide(first, second):

    if second > 0:
        rezult = first / second
        print(f'{rezult}')
    elif second == 0:
        rezult = math.inf
        print('Positive Infinity: ', rezult)


