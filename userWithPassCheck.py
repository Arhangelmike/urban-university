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

def passcheck(password):
    is_valid = False
    #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    if (len(password) <= 8 or len(password) >= 20):
        print("Неверный пароль. Нужен пароль длиной от 8 до 20 символов")
    elif not re.search("[A-Z]", password):
        print("Неверный пароль. Нужен пароль содержащий хотябы одну заглавную букву")
    elif not re.search("[a-z]", password):
        print("Неверный пароль. Нужен пароль содержащий хотябы одну строчную букву")
    elif not re.search("[1-9]", password):
        print("Неверный пароль. Нужен пароль содержащий хотябы одну цифру")
    elif not re.search("[~!@#$%^&*]", password):
        print("Неверный пароль. Нужен пароль содержащий хотябы один спецсимвол [~!@#$%^&*]")
    elif re.search("[\s]", password):
        print("Неверный пароль. Не должен содержать пробелы")
    else:
        is_valid = True
    return is_valid

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
            if  passcheck(password) == True and password == password2: # ----------------------
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                user = User(login, password, password2)
            elif passcheck(password) == False:
                print('Исправьте пароль. Повторите ввод.\n')
                continue
            elif password != password2:
                print('Пароли не совпадают. Повторите ввод.\n')
                continue
            database.add_user(user.username, user.password)
            print(database.data)
