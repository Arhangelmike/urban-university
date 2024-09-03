first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


# first_result = []
# for str3 in first_strings:
#     if len(str3) >= 5:
#         first_result.append(len(str3))


# second_result = []
# second_tuple = ()
# for str2 in first_strings:
#     for str3 in second_strings:
#         if len(str2) == len(str3):
#             second_tuple = str2, str3
#             second_result.append(second_tuple)


# third_result = {}
# for str1 in temp_strings:
#     if not len(str1) % 2:
#         third_result[str1] = len(str1)

first_result = [(len(str3)) for str3 in first_strings if len(str3) >= 5] 

second_result = [(str2, str3) for str2 in first_strings for str3 in second_strings if len(str2) == len(str3)]

temp_strings = first_strings + second_strings
third_result = {str1: len(str1) for str1 in temp_strings if len(str1) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
