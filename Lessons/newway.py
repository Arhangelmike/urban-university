import time, re, sys

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

    def __init__(self, title, duration, adult_mode = False):
        # Атриубуты:
        #            title(заголовок, строка),
        #            duration(продолжительность, секунды),
        #            time_now(секунда остановки (изначально 0)),
        #            adult_mode(ограничение по возрасту, bool (False по умолчанию))'''
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = None
        self.users = []
        self.videos = []

    def log_in(self, login, password):
        '''Метод log_in, который принимает на вход аргументы: login, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.  а сравнивается по хэшу'''
        loginuser = login
        password2 = hash(input('Введите пароль: '))
        for i in self.users:
             if i == loginuser and i+1 == password2:
                 self.current_user = login
        # print(f'{current_user}')

    def register(self, nickname, password, age):
        '''Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.'''
        self.nickname = nickname
        self.password = password
        self.age = age

        for i in self.users:
            if i in self.nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                print(f'Пользователь {nickname} НЕ существует')
                self.users.append(nickname, password, age)
                UrTube.log_in(nickname, password)

    def log_out(self):
        '''Метод log_out для сброса текущего пользователя на None.'''
        self.current_user = None


    def add(self, *args):
        '''Метод add, который принимает неограниченное кол-во объектов класса Video
        и все добавляет в videos,
        если с таким же названием видео ещё не существует.
        В противном случае  ничего не происходит.'''
        for i in args:  # для любого элемента списка проверить наличие
            if i not in self.title:  #  если i не совпадает с титлом то добавляем его в видеос
                self.videos.append(title, duration, adult_mode)

    def get_videos(self, search_substr):
        '''Метод get_videos, который принимает поисковое слово
         и возвращает список названий всех видео, содержащих поисковое слово.
         Следует учесть, не учитывать регистр'''
        self.search_substr = search_substr # принимаем подстроку которую искать надо
        for i in self.videos:  # для любого элемента в videos проверить
            if search_substr.lower() in i.lower():  # если введенная строка с убранным регистром совпадает с title или его частью
                print(f'{self.videos}')



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
    User
    Videos

while True:

    choise = int(input(f'Приветствую!. Выберите действие: \n1 - Регистрация.\n2 - Добавить видео.\n3 - Смотреть видео '))
    if choise == 1:
        nickname = input('Введите nickname: ')
        password = hash(input('Введите пароль: '))
        age = input('Введите возраст: ')
        UrTube.register(nickname, password, age)
    elif  choise == 2:
        title = input('Введите title: ')
        duration = input('Введите duration: ')
        adult_mode = input('Введите adult_mode(True\False): ')
        UrTube.add(title, duration, adult_mode)
    elif  choise == 3:
        pass


