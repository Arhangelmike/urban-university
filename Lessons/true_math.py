import math


def divide(first, second):

    if second > 0:
        rezult = first / second
        print(f'{rezult}')
    elif second == 0:
        p_inf = math.inf
        print('Positive Infinity: ', p_inf)
