my_list = ["Apple", "Banana", "Mango", "Grapefruit", "Kiwi", "Lemon", "Pineapple", "Peach", "Pear", "Nectarine", "Plum", "Tangerine", "Lime", "Apricot", "Fig", "Orange", "Papaya", "Pomegranate", "Persimmon", "Pomelo"]
#- Выведите на экран список my_list.
print("Мой лист:",  my_list)
#- Выведите на экран первый и последний элементы списка my_list.
print("Первый элемент: ", my_list[0])
print("Последний элемент: ", my_list[-1])
# - Выведите на экран подсписок my_list с третьего до пятого элементов
print("Мой подсписок my_list с третьего до пятого элементов: ", my_list[2:5])
#  - Измените значение третьего элемента списка my_list.
#print(my_list[::-1])
my_list[2]='ququmber'
#-- Выведите на экран измененный список my_list.
print("Измененный список my_list: ", my_list)

my_dict = {'Apple':'яблоко', 'Banana':'банан', 'Mango':'манго', 'Grapefruit':'грейпфрут', 'Kiwi':'киви', 'Lemon':'лемон', 'Pineapple':'ананаzzz', 'Peach':'персик', 'Pear':'груша', 'Nectarine':'нектарин', 'Plum':'слива', 'Tangerine':'мандарин', 'Lime':'лайм', 'Apricot':'абрикос', 'Fig':'инжир', 'Orange':'апельсин', 'Papaya':'папайя', 'Pomegranate':'гранат', 'Persimmon':'хурма', 'Pomelo':'помело'}
print("Словарь: ", my_dict)
print("Перевод слова: ", my_dict['Pineapple'])
my_dict['Pineapple'] ='ананас'
print("Исправленный словарь: ", my_dict)
