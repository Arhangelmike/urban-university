class Videos:

    def __init__(self, title, duration, time_now, adult_mode):
        # Атриубуты:
        #            title(заголовок, строка),
        #            duration(продолжительность, секунды),
        #            time_now(секунда остановки (изначально 0)),
        #            adult_mode(ограничение по возрасту, bool (False по умолчанию))'''
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
