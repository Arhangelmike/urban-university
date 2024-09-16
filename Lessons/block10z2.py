from threading import Thread
import time



class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.counter = 0
        self.known_enemy = 100
        print(f'{name}, на нас напали!')

    def run(self):
        
        while self.known_enemy > 0:
            self.counter += 1
            self.known_enemy = self.known_enemy - self.power
            time.sleep(1)
            print(f'{self.name} сражается {self.counter} дней..., осталось {self.known_enemy} врагов.')
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')
        


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()


print('Все бои окончены!')
