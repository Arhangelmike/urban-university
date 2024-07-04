class animal:
    def __init__(self):
        self.alive = True
        self.fed = False
        self.name = ''


class predator(animal):
    def __init__(self, name):
        self.name = name # переопределим имя класса


    def eat(self, food):
        self.food = food
        if food == True:
            animal.fed = True
            animal.alive = True
            print(f'{self.name}  съел {food.name}')# !!! predator - alive {animal.alive} fed {animal.fed}
        else:
            animal.fed = False
            animal.alive = False
            print(f'{self.name}  не стал есть {food.name} ')


class mammal(animal):

    def __init__(self, name):
        self.name = name  # переопределим имя класса

    def eat(self, food):
        self.food = food
        if food != True:
            animal.fed = True
            animal.alive = True
            print(f'{self.name}  съел {food.name}')
        else:
            animal.fed = False
            animal.alive = False
            print(f'{self.name}  не стал есть   {food.name}') #!!! mammal - alive {animal.alive} fed {animal.fed}


class plant:
    def __init__(self):
        self.edible = False
        self.name = ''


class flower(plant):
    def __init__(self, name):
        self.name = name
        plant.edible = False # для контроля того что значение верное уйдет а не дефолтное от  родительского класса


class fruit(plant):
    def __init__(self, name):
        self.name = name
        plant.edible = True


a1 = predator('Волк с Уолл-Стрит') # вызов класса хищник и передача в него имени
a2 = mammal('Хатико') # вызов класса млекопитающие и передача в него имени
p1 = flower('Цветик семицветик')# вызов класса цветы и передача в него имени
p2 = fruit('Заводной апельсин')# вызов класса фрукты и передача в него имени

print(a1.name)# распечатать имя переданное в класс
print(p1.name)# распечатать имя переданное в класс

print(a1.alive)# распечатать статус хищника жив
print(a2.fed)# распечатать статус млекопитающего накормлен
a1.eat(p1)# передать цветок в метод "кушать" хищника должен стать alive = False \ fed = False
a2.eat(p2)# передать фрукт в метод класса "кушать" млекопитающего должен стать alive = True \ fed = True
print(a1.alive)# распечатать статус хищника жив
print(a2.fed)# распечатать статус млекопитающего накормлен