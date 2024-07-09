class animal:
    alive = True
    fed = False
    name = ''


class predator(animal):
    def __init__(self, name):
        self.name = name # переопределим имя класса
        animal.__init__(self)


    def eat(self, food):


        if food.edible == True:
            self.fed = True
            self.alive = True
            print(f'{self.name}  съел {food.name}')# !!! predator - alive {animal.alive} fed {animal.fed}
        else:
            self.fed = False
            self.alive = False
            print(f'{self.name}  не стал есть {food.name} ')


class mammal(animal):

    def __init__(self, name):
        self.name = name  # переопределим имя класса
        animal.__init__(self)

    def eat(self, food):


        if plant.edible != True:
            self.fed = True
            self.alive = True
            print(f'{self.name}  съел {food.name}')
        else:
            self.fed = False
            self.alive = False
            print(f'{self.name}  не стал есть   {food.name}') #!!! mammal - alive {animal.alive} fed {animal.fed}


class plant:
    name = ''
    edible = False


class flower(plant):
    def __init__(self, name):
        self.name = name
        self.edible = False # для контроля того что значение верное уйдет а не дефолтное от  родительского класса
        plant.__init__(self)


class fruit(plant):
    def __init__(self, name):
        self.name = name
        self.edible = True
        plant.__init__(self)


a1 = predator('Волк с Уолл-Стрит') # вызов класса хищник и передача в него имени
a2 = mammal('Хатико') # вызов класса млекопитающие и передача в него имени
p1 = flower('Цветик семицветик')# вызов класса цветы и передача в него имени
p2 = fruit('Заводной апельсин')# вызов класса фрукты и передача в него имени

print(a1.name)# распечатать имя переданное в класс
print(p1.name)# распечатать имя переданное в класс

print(a1.alive)# распечатать статус хищника жив
print(a2.fed)# распечатать статус млекопитающего накормлен
a1.eat(p1)#
a2.eat(p2) #
print(a1.alive)# распечатать статус хищника жив
print(a2.fed)# распечатать статус млекопитающего накормлен