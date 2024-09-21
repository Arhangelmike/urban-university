import datetime
from multiprocessing import Pool

def read_file(name):
    all_data = []
    with open(name, 'r', encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)
# ФАЙЛЫ из списка те что у вас в той же папке что и сама программа тестовый ввод данных
filenames = ["homework1 — копия.txt", "example7.txt", "test_file.txt", "main2.txt"]
#  filenames = [f'./file {number}.txt' for number in range(1, 5)]






if __name__ == "__main__":

    # линейный
    start_t = datetime.datetime.now()
    for name in filenames:
        read_file(name)
    end_t = datetime.datetime.now()
    str1 = 'линейный метод расчета'
    delta = end_t - start_t
    print(f'{str(delta)} - {str1}')


    start_t = datetime.datetime.now()
    with Pool() as pool:
        contents = pool.map(read_file, filenames)
    end_t = datetime.datetime.now()
    str2 = 'мультипроцессорный метод расчета'
    delta = end_t - start_t
    print(f'{str(delta)} - {str2}')

    # testing output
    # for content in contents:
    #     print(content)

