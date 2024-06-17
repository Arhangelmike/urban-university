import time

class Database:
    def __init__(self):# create data structure dict + inside list
        self.data = {}
        self.passdata = {}


    def add_user(self, nickname, password, age):
        self.passdata[nickname] = password
        self.data[nickname] = age


class User:

    def __init__(self, nickname, password, password_confirm, age):
        self.nickname = nickname
        if password == password_confirm:
            self.password = password
        self.age = age


class Video:
    '''Атриубуты: title(заголовок, строка),
                duration(продолжительность, секунды),
                time_now(секунда остановки (изначально 0)),
                adult_mode(ограничение по возрасту, bool (False по умолчанию))'''

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = ' '
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False
        pass


    if __name__ == '__main__':
        database = Database()
    while True:
        choise = int(input("Приветствую!. Выберите действие: \n1 - Вход.\n2 - Регистарция.\n"))
        if choise == 1:
            login = input('Введите логин1: ')
            password = hash(input('Введите пароль1: '))
            if login in database.passdata:
                if password == database.passdata[login]:
                    print(f'Авторизация успешна!\nПриветствую {login}')
                    break
                else:
                    print('Wrong password!!!')
            else:
                print('Пользователь не найден')
        if choise == 2:
            nickname = input('Введите nickname2: ')
            password = hash(input('Введите пароль2: '))
            password2 = hash(input('Введите подтверждение пароля2: '))
            age = input('Введите возраст2: ')
            if password == password2: # ----------------------
                user = User(nickname, password, password2, age)
            elif password != password2:
                print('Пароли не совпадают. Повторите ввод.\n')
                continue
            database.add_user(user.nickname, user.password, user.age)
            print(database.data)
            print(database.passdata)

