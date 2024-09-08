from math import sqrt

def is_prime(sum_three):
    prime = True
    n = sum_three
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print('Простое число')
    else:
        print('Составное число')
    return sum_three

@is_prime
def sum_three(a, b, c):
    i = a + b + c
    return i

result = sum_three(2, 3, 6)
print(result)