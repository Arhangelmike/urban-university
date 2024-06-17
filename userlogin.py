import re
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password



if __name__ == '__main__':
    database = Database()
    while True:
        choise = int(input("Приветствую!. Выберите действие: \n1 - Вход.\n2 - Регистарция.\n"))
        if choise == 1:
            login = input('Введите логин1: ')
            password = input('Введите пароль1: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Авторизация успешна!\nПриветствую {login}')
                    break
                else:
                    print('Wrong password!!!')
            else:
                print('Пользователь не найден')
        if choise == 2:
            login = input('Введите логин2: ')
            password = input('Введите пароль2: ')
            password2 = input('Введите подтверждение пароля2: ')
            if password == password2: # ----------------------
                #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                user = User(login, password, password2)
            #elif passcheck(password) == False:
            #    print('Исправьте пароль. Повторите ввод.\n')
            #    continue
            elif password != password2:
                print('Пароли не совпадают. Повторите ввод.\n')
                continue
            database.add_user(user.username, user.password)
            print(database.data)
