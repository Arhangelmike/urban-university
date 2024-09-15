import threading

counter = 0
known_enemy = 100
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        print(f'{name}, на нас напали!')
        self.run(name, power)


    def run(self, name, power):
        global known_enemy, counter
        while known_enemy > 0:
            counter += 1
            known_enemy = known_enemy - self.power
            print(f'{self.name} сражается {counter} дней..., осталось {known_enemy} врагов.')
            #threading.Timer(1, Knight.printit).start()
            #Knight.printit()
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')
        counter = 0
        known_enemy = 100


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

print("The end")