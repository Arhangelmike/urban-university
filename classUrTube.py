class UrTube:

    def __init__(self, users, videos, current_user):
        pass

    def log_in(self):
        '''Метод log_in, который принимает на вход аргументы: login, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.  а сравнивается по хэшу'''
        pass

    def register(self):
        '''Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.'''
        pass

    def log_out(self):
        '''Метод log_out для сброса текущего пользователя на None.'''
        pass

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