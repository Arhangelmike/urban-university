# lst = '0123456789'
# lst1 = [int(i) ** 2 if int(i) % 2 == 0 else 0 for i in lst]  # список
# lst2 = (int(i) ** 2 if int(i) % 2 == 0 else 0 for i in lst)  #  генератор
# lst3 = {int(i) ** 2 if int(i) % 2 == 0 else 0 for i in lst}  # множество
# lst4 = {int(i):int(i) ** 2 for i in lst}                     # словарь
# print(lst1)
# print(lst2)
# print(lst3)
# print(lst4)
# list1 = [int(i) ** 2 if int(i) % 2 == 0 else 0 for i in range(10000000)]  # список
# gen = (int(i) ** 2 if int(i) % 2 == 0 else 0 for i in range(10000000))    #  генератор
# print(list1.__sizeof__())
# print(gen.__sizeof__())

