def is_prime(sum_three):
    def wrapper(a, b, c):
        res = sum_three(a, b, c)
        for i in range(2, int(res ** 0.5 + 1)):
            if res % i == 0:
                print("Составное")
                break
        else:
            print('Простое')
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    i = a + b + c
    return i

result = sum_three(2, 3, 6)
print(result)