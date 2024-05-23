# Создайте новую функцию def test... с произвольным числом параметров разного типа, функция должна распечатывать
# эти параметры внутри своего тела
# Создайте рекурсивную функцию, которая будет считать факториал от числа n

# не рекурсия
#def test(number):
#    fact = 1
#    for i in range(1, number+1):
#        fact = fact * i
#    print(fact)


def test(n):
    n=0
    if n == 1:
        return n
    else:
        return n*test(n-1)


n= int(input('Введите число: '))
print(test(n))
