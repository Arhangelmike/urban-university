from threading import Thread
import time

statist = []
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.counter = 0
        self.known_enemy = 100
        print(f'{name}, на нас напали!')

    def run(self):
        global statist
        while self.known_enemy > 0:
            self.counter += 1
            self.known_enemy = self.known_enemy - self.power
            #time.sleep(1)
            print(f'{self.name} сражается {self.counter} дней..., осталось {self.known_enemy} врагов.')
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')

        statist.append(self.name)
        statist.append(self.counter)
        statist.append(self.power)
        # print(statist)
        return statist

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

a1 = str(statist[2]/statist[5])
a2 = str(statist[5]/statist[2])
if statist[2] >= statist[5]:
    print(f'{statist[0]} сильнее {statist[3]} в {a1} разa')
else:
    print(f'{statist[3]} сильнее {statist[0]} в {a2} разa')
print('Все бои окончены!')
