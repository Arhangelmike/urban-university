'''. Задайте переменные разных типов данных:
 Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
 Выполните операции вывода кортежа immutable_var на экран.
'''
immutable_var= (3, 4, 5, True, 546, 'string')
print(immutable_var)
# Попытайтесь изменить элементы кортежа immutable_var.
# immutable_var[0]=9
# OUTPUT:
'''(3, 4, 5, True, 546, 'string')
Traceback (most recent call last):
  File "C:\Users\user\PycharmProjects\.....homework4.py", line 8, in <module>
    immutable_var[0]=9
    ~~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
Объяснение: ошибка из за того что кортеж не поддерживает изменение элементов.

'''
 # Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list=[5, 32, 10, 11, 9]
 # Измените элементы списка mutable_list.
mutable_list[2]=67
# Выведите на экран измененный список mutable_list.
print(mutable_list)