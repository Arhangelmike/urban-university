def custom_write(file_name: str, strings: list):
    strings_dict = {}
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        strings_dict[(strings.index(i) + 1, file.tell())] = i
        file.write(f'{i}\n')
    file.close()
    return strings_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


strings_positions = custom_write('C:/Users/user/Pictures/1/file_name1.txt', info)
for elem in strings_positions.items():
    print(elem)
