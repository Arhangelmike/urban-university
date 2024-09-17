import threading, time, random
from queue import Queue
from datetime import datetime


class Table:
    def __init__(self, number):
        self.number  = number
        self.guest = None

class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        self.waiting = random.randint(3,10)
        time.sleep(self.waiting)
class Cafe:

    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()



    def guest_arrival(self, *guests):
        self.guests = list(guests)


    def discuss_guests(self, *args):
        pass


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()