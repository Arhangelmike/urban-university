class User:

'''Каждый объект класса User должен обладать следующими атрибутами и методами'''

    def __init__(self, nickname, password, age):
        # Атриубуты:
        #             nickname(имя пользователя, строка),
        #             password(в хэшированном виде, число),
        #             age(возраст, число)
        self.nickname = nickname
        self.password = password
        self.age = age
