# version 1
str1= 'это моя строка'
str2= 'это новая строка'
#Выведите первый символ.
print(str1[0])
#Выведите последний символ (используя отрицательный индекс).
print(str1[-1])
#Выведите подстроку с третьего по пятый символы (то есть со второго по четвёртый индекс.
# Важно помнить что в записи [4:8] выведется с 4 по 7 индекс).
print(str1[2:5])
#Выведите строку наоборот
print(str1[::-1])
#Выведите длину строки (функция len).
print(len(str1))
#Соедините строки 'это новая строка' и 'это моя строка' (в той же последовательности) и выведите результат на экран.
print(str2 +" "+ str1)