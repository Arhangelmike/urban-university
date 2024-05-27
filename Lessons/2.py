# исходные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# функция однократного прогона листа через распаковку содержимого внутренних листов\сетов\словарей\туплов
def raspskovka(from_dict):
    for i in from_dict:
        if isinstance(i, list):
            temp_list1 = list(i)
            from_dict.remove(i)
            from_dict = from_dict + temp_list1
        elif isinstance(i, tuple):
            temp_list2 = list(i)
            from_dict.remove(i)
            from_dict.append(temp_list2)
        elif isinstance(i, set):
            temp_list3 = list(i)
            from_dict.remove(i)
            from_dict.append(temp_list3)
        elif isinstance(i, dict):
            con_lis_keys = list(i.keys())
            con_lis_value = list(i.values())
            temp_list = con_lis_value + con_lis_keys
            from_dict.remove(i)
            from_dict.append(temp_list)
    return(from_dict)

#
from_dict = data_structure
print(from_dict)
TYPES = [int, str]
# обращение к функции столько раз cколько элементов листа не относящихся к типам: int и  str

while any(type(x) not in TYPES for x in from_dict):
    from_dict = raspskovka(from_dict)

print(from_dict)

# считаем количество чисел и количество символов в строках
num_sum = 0
str_len = ''
for i in from_dict:
    if isinstance(i, int):
        num_sum = num_sum + i
    elif isinstance(i, str):
        str_len = str_len + i


print("Все строки: ", len(str_len))
print("Все числа : ", num_sum)
print("подсчёта суммы всех чисел и длин всех строк:", num_sum + len(str_len))

