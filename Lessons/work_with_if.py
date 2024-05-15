# эксперимент с вложенным if
'''user_input = input("Enter your age:" +"\n")
if user_input.isdigit():
        # print("Is a number")
    age=int(user_input)
    if age >=18:
          print('Your are 18+')
    else:
          print('Your are not 18+')
else:
        print("Not an age")'''
''' 3.Напишите и запустите блок кода, посмотрите на результат выполнения программы'''
x=38
print('дратути!')
if x<0:
     print('Меньше нуля')

print('дотвидания!')
'''OUTPUT: 
дратути!
дотвидания!
'''
'''4. Напишите и запустите блок кода, посмотрите на результат выполнения программы'''

a, b = 10, 5
if a > b:
    print(' a > b ')
if (a > b) and (a > 0 or b < 1000):
    print('успех')
if 5 < b and b < 10:
    print('успех2')
    '''OUTPUT: 
 a > b 
успех
    '''
# задания 5 нет
# 6. Напишите и запустите блок кода, посмотрите на результат выполнения программы
# можно сравнивать - числа, строки, списки, вообще -
if '34' > '123':
    print('успех3')
if  '123' > '12':
    print('успех4')
if  [1, 2] > [1, 1]:
    print('успех5')

'''OUTPUT: 
успех3
успех4
успех5
    '''
# 7. Напишите и запустите блок кода, посмотрите на результат выполнения программы
# что нельзя сравнивать - разные типы  !!!!!!КОД ВЫЗЫВАЮЩИЙ ОШИБКИ ЗАКОМЕНТИРОВАН!!!!!!

#if  '6' > 5:
#    print('успех4')
'''OUTPUT:
     if  '6' > 5:
        ^^^^^^^
      TypeError: '>' not supported between instances of 'str' and 'int' '''
#if  [5, 6] > 5:
#    print('успех6')
'''OUTPUT:
    if  [5, 6] > 5:
        ^^^^^^^^^^
TypeError: '>' not supported between instances of 'list' and 'int' '''
# но
if  '6' != 5:
    print('успех7')

'''OUTPUT: 
успех7
    '''
# 8. Загрузите на свой GitHub репозиторий файл с кодом. Прикрепите ссылку на GitHub репозитория к домашнему заданию.
#https://github.com/Arhangelmike/urban-university/blob/master/Lessons/work_with_if.py
#