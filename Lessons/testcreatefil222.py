file_name = 'C:/Users/user/Pictures/1/file_name1.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line)
print(file.closed)