from random import choice

# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding='UTF-8') as file:
            for element in data_set:
                file.write(str(element) + '\n')

    return write_everything


write = get_advanced_writer('test_file.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:

class MysticBall:
    def __init__(self, *words: str):
        self.words = words

    def __call__(self):
        return choice(self.words)

# test_text = input ("Введите вопрос: ") #  Например - Есть ли жизнь на Марсе?
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())