# def is_prime(sum_three):
#     def wrapper(a, b, c):
#         res = sum_three(a, b, c)
#         for i in range(2, int(res ** 0.5 + 1)):
#             if res % i == 0:
#                 print("Составное")
#                 break
#         else:
#             print('Простое')
#
#         return res
#
#     return wrapper

def is_prime(sum_three):
    def wrapper(*args):
        res = sum_three(*args)
        for i in range(2, int(res ** 0.5 + 1)):
            if res % i == 0:
                print("Составное")
                break
        else:
            print('Простое')

        return res

    return wrapper


# @is_prime
# def sum_three(a, b, c):
#     return a + b + c
@is_prime
def sum_three(*args: int):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
