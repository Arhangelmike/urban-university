data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def con_dict_to_list(from_dict):
    con_lis_keys = list(from_dict.keys())
    con_lis_value = list(from_dict.values())
    from_dict = con_lis_value + con_lis_keys
    return (from_dict)


from_dict = data_structure
print(from_dict)


for j in range(11):
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
            temp_list = con_dict_to_list(i)
            from_dict.remove(i)
            from_dict.append(temp_list)
    print(from_dict)

num_sum = 0
str_len = ''

for i in from_dict:
    if isinstance(i, int):
        num_sum = num_sum + i
    elif isinstance(i, str):
        str_len = str_len + i
        result = ''.join([k for k in str_len if not k.isdigit()])
        # Забрать все буквы в строку
        result2 = ''.join([k for k in str_len if k.isdigit()])
        # Забрать число из строки !! проверить если их несколько то сложить дописать код
        #print(str_len)
        #print(result)
        #print(result2)
# не пододбрал варианта условия (пока в элементах списка не останеться элементы типа int и str делать)

num_sum = num_sum + int(result2)
str_len2 = len(result)
#print(str_len2)
#print(num_sum)
print(num_sum + str_len2)
