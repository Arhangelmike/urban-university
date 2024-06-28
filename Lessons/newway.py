
import time


class User:

    def __init__(self, nickname: str, password: str, age: int):
        # Атриубуты:
        #             nickname(имя пользователя, строка),
        #             password(в хэшированном виде, число),
        #             age(возраст, число)
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
        return f"{self.current_user}"

    def register(self, nickname: str, password: str, age: int):
        password = str(hash(password))
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if not any(v.title == i.title for v in self.videos):
                self.videos.append(i)

    def get_videos(self, search_substr):
        search_result = []
        for i in self.videos:
            if search_substr.lower() in i.title.lower():
                search_result.append(i.title)
        return search_result

    def watch_video(self, i: str):
        if self.current_user is not None and int(self.current_user.age) < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user is not None and int(self.current_user.age) > 18:
            for video in self.videos:
                if i in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        elif self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')