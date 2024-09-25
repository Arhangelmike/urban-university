# from multiprocessing import Pool
#
# # Функция, которая будет применена к каждому элементу
# def square(n):
#     return n * n
#
# if __name__ == '__main__':
#     # Создание пула из 4 процессов
#     with Pool(processes=4) as pool:
#         # Входной список значений
#         values = [1, 2, 3, 4, 5]
#         # Применение функции square к каждому элементу в списке параллельно
#         results = pool.map(square, values)
#         print(results)


# import multiprocessing
# from multiprocessing import Pool
#
# def read_file(filename):
#     with open(filename, 'r', encoding="utf-8") as file:
#         content = file.read()
#     return content
#     # You can perform any file reading operations here
#
# if __name__ == "__main__":
#     # ФАЙЛЫ из списка те что у вас в той же папке что и сама программа
#     filenames = ["homework1 — копия.txt", "example7.txt", "test_file.txt", "main2.txt"]
#
#     with Pool() as pool:
#         contents = pool.map(read_file, filenames)
#
#     for content in contents:
#         print(content)
#
#
# import logging
# import multiprocessing
# from multiprocessing import Process, Lock
#
#
# def printer(item, lock):
#     """
#     Выводим то что передали
#     """
#     lock.acquire()
#     try:
#         print(item)
#     finally:
#         lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'foxtrot', 10]
#     multiprocessing.log_to_stderr()
#
#     logger = multiprocessing.get_logger()
#     logger.setLevel(logging.INFO)
#
#     for item in items:
#         p = Process(target=printer, args=(item, lock))
#         p.start()

#
# from multiprocessing import Pool
#
#
# def doubler(number):
#     return number * 2
#
#
# if __name__ == '__main__':
#     numbers = [5, 10, 20]
#     pool = Pool(processes=3)
#     print(pool.map(doubler, numbers))

import requests