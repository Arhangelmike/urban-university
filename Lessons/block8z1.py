def add_everything_up(a, b):
    try:
        sum1 = a + b
        return round(sum1, 3)
    except TypeError:
        return f'{a}{b}'
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
