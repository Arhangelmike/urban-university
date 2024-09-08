def is_prime(sum_three):
    return sum_three


def sum_three(*args):
    for i in args:
        i +=i
    print(i)
    return i

result = sum_three(2, 3, 6)
print(result)