first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

'''В переменную first_result запишите список,
состоящий из длин строк списка first_strings, при условии, 
что длина строк не менее 5 символов.'''

first_result = []
for str3 in first_strings:
    if len(str3) >= 5:
        first_result.append(len(str3))

print(first_result)

'''В переменную second_result запишите список созданный при помощи 
сборки состоящий из пар слов(кортежей) одинаковой длины. 
Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)'''

second_result = []




