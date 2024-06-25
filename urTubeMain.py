import time, re, sys
class dbdata:
    def __init__(self):
        self.data = {}
        self.passdata = {}

    def add_user(self, nickname, password, age):
        self.passdata[nickname] = password
        self.agedata[nickname] = age

    def add_video(self, title, adult_mode, duration):
         pass

class User:

    def __init__(self, nickname, password, age):
        # Атриубуты:
        #             nickname(имя пользователя, строка),
        #             password(в хэшированном виде, число),
        #             age(возраст, число)
        self.nickname = nickname
        self.password = password
        self.age = age

class Videos:

    def __init__(self, title, duration, time_now, adult_mode):
        # Атриубуты:
        #            title(заголовок, строка),
        #            duration(продолжительность, секунды),
        #            time_now(секунда остановки (изначально 0)),
        #            adult_mode(ограничение по возрасту, bool (False по умолчанию))'''
        self.title = ''
        self.duration = 0
        self.time_now = 0
        self.adult_mode = False

class UrTube:

    def __init__(self, users, videos, current_user):
        self.users  =   users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        '''Метод log_in, который принимает на вход аргументы: login, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.  а сравнивается по хэшу'''
        self.login = login
        self.password = password
        if password == dbdata.passdata[login]:
            current_user = login
            print(f'{current_user}')

    def register(self, nickname, password, age):
        '''Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.'''
        self.nickname = nickname
        self.password = password
        self.age = age

        login = nickname
        if login in dbdata.passdata:
            print(f'Пользователь {nickname} уже существует')
        else:
            print(f'Пользователь {nickname} НЕ существует')
            dbdata.add_user(nickname, password, age)
            UrTube.log_in(nickname, password)

    def log_out(self):
        '''Метод log_out для сброса текущего пользователя на None.'''
        current_user = None
        return current_user

    def add(self):
        '''Метод add, который принимает неограниченное кол-во объектов класса Video
        и все добавляет в videos,
        если с таким же названием видео ещё не существует.
        В противном случае  (if exist) ничего не происходит.'''
        pass

    def get_videos(self):
        '''Метод get_videos, который принимает поисковое слово
         и возвращает список названий всех видео, содержащих поисковое слово.
         Следует учесть, не учитывать регистр'''
        pass

    def watch_videos(self):
        '''Метод watch_video, который принимает название фильма,
        если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.

        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        '''
        pass



if __name__ == '__main__':
    database = dbdata()
while True:
    choise = int(input(f'Приветствую!. Выберите действие: \n1 - Вход.\n2 - Регистарция.\n '))
    if choise == 1:
    nickname = input('Введите nickname2: ')
    password = hash(input('Введите пароль2: '))
    password2 = hash(input('Введите подтверждение пароля2: '))
    age = input('Введите возраст2: ')
    if password == password2:  # ----------------------
        UrTube.register(nickname, password, age)
    elif password != password2:
        print('Пароли не совпадают. Повторите ввод.\n')


